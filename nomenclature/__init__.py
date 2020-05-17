from pathlib import Path
import logging
import yaml
from pyam import IamDataFrame

logger = logging.getLogger(__name__)

DEF_PATH = Path('nomenclature/definitions')


# set up logging formatting
stderr_info_handler = logging.StreamHandler()
formatter = logging.Formatter('%(name)s - %(levelname)s: %(message)s')
stderr_info_handler.setFormatter(formatter)
logger.addHandler(stderr_info_handler)


def _parse_yaml(path, file='**/*', ext='.yaml'):
    """Parse yaml files in path (all files in subfolders if `file='**/*'`)"""
    dct = {}
    for f in path.glob(f'{file}{ext}'):
        with open(f, 'r') as stream:
            _dct = yaml.safe_load(stream)
            # add `file` attribute to each dictionary
            for key, value in _dct.items():
                value['file'] = str(f)
            dct.update(_dct)
    return dct


variables = _parse_yaml(DEF_PATH / 'variable')
"""Dictionary of variables"""


regions = _parse_yaml(DEF_PATH / 'region')
"""Dictionary of all regions"""


countries = _parse_yaml(DEF_PATH / 'region', 'countries')
"""Dictionary of countries"""


iso_mapping = dict(
    [(countries[c]['iso3'], c) for c in countries]
    + [(countries[c]['iso2'], c) for c in countries]
    # add alternative iso2 codes used by the European Commission to the mapping
    + [(countries[c]['iso2_alt'], c) for c in countries
       if 'iso2_alt' in countries[c]]
)
"""Dictionary of iso2/iso3/alternative-iso2 codes to country names"""


def _add_to(_mapping, key, value):
    """Add key-value to mapping"""
    if key not in mapping:
        _mapping[key] = value
    elif isinstance(value, list):
        _mapping[key] += value
    return _mapping[key]


nuts_hierarchy = dict()
"""Hierarchical dictionary of nuts region classification"""
for _n3, mapping in _parse_yaml(DEF_PATH / 'region', 'nuts3').items():
    _country, _n1, _n2 = mapping['country'], mapping['nuts1'], mapping['nuts2']
    country_dict = _add_to(nuts_hierarchy, _country, {_n1: dict()})
    _n1_dict = _add_to(country_dict, _n1, {_n2: list()})
    _add_to(_n1_dict, _n2, [_n3])


subannual = _parse_yaml(DEF_PATH / 'subannual')
"""Dictionary of subannual timeslices"""


def validate(df):
    """Validate that all columns of a dataframe follow the nomenclature

    Parameters
    ----------
    df : path to file, pandas.DataFrame, pyam.IamDataFrame (or castable object)
        A timeseries dataframe following the common data format

    Returns
    -------
    bool
        Return `True` if all column entries in `df` are valid
        or `False` otherwise
    """
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
    msg = 'The following {} are not defined in the nomenclature:\n    {}'
    for col, codelist, ext in cols:
        invalid = [c for c in df.data[col].unique() if c not in codelist]
        if invalid:
            success = False
            logger.warning(msg.format(col + ext, invalid))

    return success
