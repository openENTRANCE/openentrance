import pandas as pd
from pyam import IamDataFrame
from nomenclature import validate


TEST_DF = pd.DataFrame([
    ['model_a', 'scen_a', 'Europe', 'Primary Energy', 'EJ/yr', 1, 6.],
],
    columns=['model', 'scenario', 'region', 'variable', 'unit', 2005, 2010]
)


def test_validate():
    # test simple validation
    assert validate(TEST_DF)


def test_validate_fail():
    # test that simple validation fails on variable and region dimension
    df = IamDataFrame(TEST_DF)
    assert not validate(df.rename(variable={'Primary Energy': 'foo})
    assert not validate(df.rename(region={'Europe': 'foo})


def test_validate_directional():
    # test that validation works as expected with directional data
    assert validate(IamDataFrame(TEST_DF).rename(region={'Europe': 'Austria>Germany'}))
    assert not validate(IamDataFrame(TEST_DF).rename(region={'Europe': 'Austria>foo'}))