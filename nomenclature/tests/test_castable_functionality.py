import pandas as pd
from pyam import IamDataFrame
from nomenclature import _validate_time_dt
from nomenclature import validate


TEST_DF = pd.DataFrame([
    ['model_a', 'scen_a', 'Europe', 'Primary Energy', 'EJ/yr', 1, 6, 12],
],
    columns=['model', 'scenario', 'region', 'variable', 'unit',
             '2005-06-17 00:00+01:00', '2010-07-21 12:00+01:00', '2015-07-21 12:00+01:00'])
df = IamDataFrame(TEST_DF)


def test_validate_time_dt():
    assert _validate_time_dt(df.data.time)
