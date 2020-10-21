from pathlib import Path
import logging
import yaml
from pyam import IamDataFrame

# set up logging formatting
logger = logging.getLogger(__name__)
stderr_info_handler = logging.StreamHandler()
formatter = logging.Formatter('%(name)s - %(levelname)s: %(message)s')
stderr_info_handler.setFormatter(formatter)
logger.addHandler(stderr_info_handler)


# path to nomenclature definitions
DEF_PATH = Path(__file__).parent / 'definitions'

# auxiliary dictionary to add CCS subcategories
CCS_TYPES = [
    ('w/ CCS', 'with a CO2 capture component'),
    ('w/o CCS', 'with freely vented CO2 emissions')
]


def _parse_yaml(path, file='**/*', ext='.yaml'):
    """Parse `file` in `path` (or all files in subfolders if `file='**/*'`)"""
    dct = {}
    for f in path.glob(f'{file}{ext}'):
        with open(f, 'r', encoding='utf-8') as stream:
            _dct = yaml.safe_load(stream)
            # add `file` attribute to each element in the dictionary
            for key, value in _dct.items():
                value['file'] = str(f)
            dct.update(_dct)
    return dct


def _copy_dict(dct, description):
    """Return a copy of `dct` after overwriting the `description`"""
    _dct = dct.copy()
    _dct['description'] = description
    return _dct


variables = dict()
"""Dictionary of variables"""

# read all variable definitions to auxiliary dictionary
_variables = _parse_yaml(DEF_PATH / 'variable')

# explode <Fuels> tags to full lists
fuel_types = _variables.pop('<Fuel>')
# explode <industry> tags to full lists
industry_types = _variables.pop('<Industry>')
# explode <product> tags to full lists
product_types = _variables.pop('<Product>')
d = 'description'
key_types = [
    ('<Fuel>', fuel_types),
    ('<Industry>', industry_types),
    ('<Product>', product_types)
]
for key, value in _variables.items():
    for k, types in key_types:
        if k in key:
            for f, attr in types.items():
                # ignore the file attribute in the <Fuel> dictionary
                if f == 'file':
                    continue

                # change generic tag to specific item in key and description
                _key = key.replace('<Fuel>', f)
                _description = value[d].replace('<this fuel>', attr[d].lower())
                variables[_key] = _copy_dict(value, _description)

                # add CCS subcategories (if applicable)
                if 'ccs' in attr and attr['ccs'] is True:
                    for sub, desc in CCS_TYPES:
                        _key_ccs = f'{_key}|{sub}'
                        _description_ccs = f'{_description} {desc}'
                        variables[_key_ccs] = _copy_dict(
                            value, _description_ccs)

        # otherwise, move items from auxiliary to public dictionary
        else:
            variables[key] = _variables[key]

# for key, value in _variables.items():
#     # if the key contains the tag, loop over all fuel types to add mapping
#     if '<Fuel>' in key:
#         for f, attr in fuel_types.items():
#             # ignore the file attribute in the <Fuel> dictionary
#             if f == 'file':
#                 continue
#
#             # change generic tag to specific item in key and description
#             _key = key.replace('<Fuel>', f)
#             _description = value[d].replace('<this fuel>', attr[d].lower())
#             variables[_key] = _copy_dict(value, _description)
#
#             # add CCS subcategories (if applicable)
#             if 'ccs' in attr and attr['ccs'] is True:
#                 for sub, desc in CCS_TYPES:
#                     _key_ccs = f'{_key}|{sub}'
#                     _description_ccs = f'{_description} {desc}'
#                     variables[_key_ccs] = _copy_dict(value, _description_ccs)
#
#     # if the key contains the tag, loop over all industry types to add mapping
#     if '<Industry>' in key:
#         for f, attr in industry_types.items():
#             # ignore the file attribute in the <industry> dictionary
#             if f == 'file':
#                 continue
#             # change the generic tag to specific item in key and description
#             _key = key.replace('<Industry>', f)
#             _description = value[d].replace('<this industry>', attr[d].lower())
#             variables[_key] = _copy_dict(value, _description)
#
#     # if the key contains the tag, loop over all product types to add mapping
#     if '<Product>' in key:
#         for f, attr in product_types.items():
#             # ignore the file attribute in the <product> dictionary
#             if f == 'file':
#                 continue
#             # change the generic tag to specific item in key and description
#             _key = key.replace('<Product>', f)
#             _description = value[d].replace('<this product>', attr[d].lower())
#             variables[_key] = _copy_dict(value, _description)
#
#     # otherwise, move items from auxiliary to public dictionary
#     else:
#         variables[key] = _variables[key]

# remove auxiliary dictionary
del _variables

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


def _add_to(mapping, key, value):
    """Add key-value to mapping"""
    if key not in mapping:
        mapping[key] = value
    elif isinstance(value, list):
        mapping[key] += value
    return mapping[key]


def _create_nuts3_hierarchy():
    """Parse nuts3.yaml and create hierarchical dictionary"""
    hierarchy = dict()
    keys = ['country', 'nuts1', 'nuts2']
    for n3, mapping in _parse_yaml(DEF_PATH / 'region', 'nuts3').items():
        country, n1, n2 = [mapping.get(i) for i in keys]
        country_dict = _add_to(hierarchy, country, {n1: dict()})
        n1_dict = _add_to(country_dict, n1, {n2: list()})
        _add_to(n1_dict, n2, [n3])
    return hierarchy


nuts_hierarchy = _create_nuts3_hierarchy()
"""Hierarchical dictionary of nuts region classification"""


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
    if not isinstance(df, IamDataFrame):
        df = IamDataFrame(df)
    success = True

    # set up list of dimension (columns) to validate (`subannual` is optional)
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

        # check the entries in the invalid list related to directional data
        if col == 'region':
            invalid = [i for i in invalid if not _validate_directional(i)]

        # check if any entries in the column are invalid and write to log
        if invalid:
            success = False
            logger.warning(msg.format(col + ext, invalid))

    return success


def _validate_directional(x):
    """Utility function to check whether region-to-region code is valid"""
    x = x.split('>')
    return len(x) == 2 and all([i in regions for i in x])
