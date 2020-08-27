import pandas as pd
from pyam import IamDataFrame
from nomenclature import swap_time_for_subannual


TEST_DF = pd.DataFrame([
    ['model_a', 'scen_a', 'Europe', 'Primary Energy', 'EJ/yr', 1, 6.],
],
    columns=['model', 'scenario', 'region', 'variable', 'unit',
             '2005-06-17T00:00+0100', '2010-07-21T12:00+0100'])
df = IamDataFrame(TEST_DF)


def test_swap_time_for_subannual():
    # test transforming of IamDataFrame in datetime domain to year + subannual
    obs = swap_time_for_subannual(df).data
    obs_year = list(obs['year'].values)
    obs_subannual = list(obs['subannual'].values)
    assert obs_year == [2005, 2010] and \
        obs_subannual == ['06-17 00:00+0100', '07-21 12:00+0100']

