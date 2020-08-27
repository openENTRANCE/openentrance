from pathlib import Path
import logging
import yaml

import pandas as pd
from pyam import IamDataFrame
from datetime import datetime, timedelta


# set up logging formatting
logger = logging.getLogger(__name__)
stderr_info_handler = logging.StreamHandler()
formatter = logging.Formatter('%(name)s - %(levelname)s: %(message)s')
stderr_info_handler.setFormatter(formatter)
logger.addHandler(stderr_info_handler)


# path to nomenclature definitions
DEF_PATH = Path(__file__).parent / 'definitions'


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

    msg = 'The following {} are not defined in the nomenclature:\n    {}'

    # set up list of dimension (columns) to validate (`subannual` is optional)
    cols = [
        ('region', regions, 's'),
        ('variable', variables, 's')
    ]
    if 'subannual' in df.data.columns:
        cols.append(('subannual', subannual, ' timeslices'))

    # validate the time domain if a dataframe has continuous 'datetime' format
    if df.time_col == 'time':
        success = _validate_time_dt(df.data.time)

    # validate all (other) columns
    for col, codelist, ext in cols:
        invalid = [c for c in df.data[col].unique() if c not in codelist]

        # check if entries in the invalid list are related to directional data
        if col == 'region' and invalid:
            invalid = [i for i in invalid if not _validate_directional(i)]

        # check if entries in the invalid list for subannual are datetime
        if col == 'subannual' and invalid:
            # downselect to any data that might be invalid
            data = df.filter(subannual=invalid)\
                .data[['year', 'subannual']].drop_duplicates()
            # call utility whether subannual can be cast to datetime
            invalid, success = _validate_subannual_dt(
                list(zip(data['year'], data['subannual']))
            )

        # check if any entries in the column are invalid and write to log
        if invalid:
            success = False
            logger.warning(msg.format(col + ext, invalid))

    return success


def swap_time_for_subannual(df):
    """Convert an IamDataFrame with `datetime` domain to `year + subannual`"""
    if df.time_col != 'time':
        raise ValueError('The IamDataFrame does not have `datetime` domain!')

    _data = df.data
    _data['year'] = [x.year for x in _data.time]
    _data['subannual'] = [x.strftime('%m-%d %H:%M%z') for x in _data.time]
    _data.drop(columns='time', inplace=True)

    return IamDataFrame(_data)


def _validate_time_dt(x):
    """Utility function to validate datetime format"""
    if not all([isinstance(i, datetime) for i in x]):
        logger.warning('Time domain is not given in `datetime` format!')
        return False

    return _validate_timezone(x)


def _validate_timezone(x):
    """Utility function to validate expected timezone format"""
    tz_name = 'Central European time'
    exp_tz = 'UTC+01:00'
    exp_offset = timedelta(seconds=3600)

    if all([t.tzname() == exp_tz or t.utcoffset() == exp_offset for t in x]):
        return True
    else:
        logger.warning(f'Time domain is not given in {tz_name} ({exp_tz})!')
        return False


def _validate_subannual_dt(x):
    """Utility function to separate and validate datetime format"""
    valid_dt, invalid_tz, invalid, success = [], False, set(), False
    for (y, s) in x:
        try:  # casting to Central European datetime
            valid_dt.append(datetime.strptime(f'{y}-{s}', '%Y-%m-%d %H:%M%z'))
        except ValueError:
            try:  # casting to UTC datetime
                datetime.strptime(f'{y}-{s}', '%Y-%m-%d %H:%M')
                invalid_tz = True
                logger.warning(
                    f'Valid datetime format but without timezone given!')

            except ValueError:  # if casting to datetime fails, return invalid
                invalid.add(s)

    if _validate_timezone(valid_dt) and not invalid and not invalid_tz:
        success = True

    return list(invalid), success


def _validate_directional(x):
    """Utility function to check whether region-to-region code is valid"""
    x = x.split('>')
    return len(x) == 2 and all([i in regions for i in x])
