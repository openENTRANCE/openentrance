from pathlib import Path
import logging
import yaml
from pyam import IamDataFrame

logger = logging.getLogger(__name__)

DEF_PATH = Path('nomenclature/definitions')
REGION_PATH = DEF_PATH / 'region'

warn_invalid = 'The following {} are not defined in the nomenclature:\n    {}'

__all__ = [
    'variables',
]

stderr_info_handler = logging.StreamHandler()
formatter = logging.Formatter('%(name)s - %(levelname)s: %(message)s')
stderr_info_handler.setFormatter(formatter)
logger.addHandler(stderr_info_handler)

# validation function

def validate(df):

    df = IamDataFrame(df)
    success = True

    # set up list of dimension (columns) to validate
    cols = [
        ('region', regions, 's'),
        ('variable', variables, 's')
    ]
    if 'subannual' in df.data.columns:
        cols.append(('subannual', subannual, ' timeslices'))

    # iterate over dimensions and perform validation
    for col, codelist, ext in cols:
        invalid = [c for c in df.data[col].unique() if c not in codelist]
        if invalid:
            success = False
            logger.warning(warn_invalid.format(col + ext, invalid))

    return success


# variables

# dictionary of variables
variables = {}
for file in (DEF_PATH / 'variable').glob('**/*.yaml'):
    with open(file, 'r') as stream:
        variables.update(yaml.safe_load(stream))

# regions

# dictionary of regions
regions = {}
for file in REGION_PATH.glob('**/*.yaml'):
    with open(file, 'r') as stream:
        regions.update(yaml.safe_load(stream))
# dictionary of countries only
with open(REGION_PATH / 'countries.yaml', 'r') as stream:
    countries = yaml.safe_load(stream)

# translate `countries` to mapping (dictionary) of iso2 and iso3
iso_mapping = dict(
    [(countries[c]['iso3'], c) for c in countries]
    + [(countries[c]['iso2'], c) for c in countries]
    # add alternative iso2 codes used by the European Commission to the mapping
    + [(countries[c]['iso2_alt'], c) for c in countries
       if 'iso2_alt' in countries[c]]
)

# build hierarchical dictionary of nuts region classification

# load nuts3 codelist from file
with open(REGION_PATH / 'nuts3.yaml', 'r') as stream:
    nuts3_codelist = yaml.load(stream, Loader=yaml.FullLoader)


# auxiliary function to add key-value to object and return
def _add_to(mapping, key, value):
    if key not in mapping:
        mapping[key] = value
    elif isinstance(value, list):
        mapping[key] += value
    return mapping[key]


# iterate over nuts3 codelist and recursively add items to the hierarchy dict
nuts_hierarchy = dict()
for _n3, mapping in nuts3_codelist.items():
    _country, _n1, _n2 = mapping['country'], mapping['nuts1'], mapping['nuts2']
    country_dict = _add_to(nuts_hierarchy, _country, {_n1: dict()})
    _n1_dict = _add_to(country_dict, _n1, {_n2: list()})
    _add_to(_n1_dict, _n2, [_n3])


# subannual timeslices

# dictionary of timeslices
subannual = {}
for file in (DEF_PATH / 'subannual').glob('**/*.yaml'):
    with open(file, 'r') as stream:
        subannual.update(yaml.safe_load(stream))
