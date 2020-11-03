import pandas as pd
from nomenclature import _validate_time_dt


def test_validate_time_dt():
    # list of datetimes in expected format
    x = ['2005-06-17 00:00+01:00', '2010-07-21 12:00+01:00']
    assert _validate_time_dt(pd.to_datetime(x))

    # list of datetimes with missing timezone info
    x = ['2005-06-17 00:00', '2010-07-21 12:00+01:00']
    assert not _validate_time_dt(pd.to_datetime(x))

    # list of datetimes with wrong timezone info
    x = ['2005-06-17 00:00+02:00', '2010-07-21 12:00+01:00']
    assert not _validate_time_dt(pd.to_datetime(x))
