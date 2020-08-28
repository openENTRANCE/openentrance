import pandas as pd
from pyam import IamDataFrame
from nomenclature import validate


TEST_DF = pd.DataFrame([
    ['model_a', 'scen_a', 'Europe', 'Primary Energy', 'EJ/yr', 1, 6.],
],
    columns=['model', 'scenario', 'region', 'variable', 'unit', 2005, 2010])
df = IamDataFrame(TEST_DF)


def test_validate():
    # test simple validation
    assert validate(df)


def test_validate_fail():
    # test that simple validation fails on variable and region dimension
    assert not (validate(df.rename(variable={'Primary Energy': 'foo'})))
    assert not (validate(df.rename(region={'Europe': 'foo'})))


def test_validate_directional():
    # test that validation works as expected with directional data
    assert validate(df.rename(region={'Europe': 'Austria>Germany'}))
    assert not validate(df.rename(region={'Europe': 'Austria>foo'}))

    # test that directional data with more than one `>` fails
    assert not validate(df.rename(region={'Europe': 'Austria>Italy>France'}))


def test_validate_subannual_months():
    # test that validation works as expected with months
    # (and representative timeslices generally)
    assert validate(IamDataFrame(TEST_DF, subannual='January'))
    assert not validate(IamDataFrame(TEST_DF, subannual='foo'))


def test_validate_subannual_datetime_as_subannual():
    # test that validation works as expected with continuous time as subannual
    assert validate(IamDataFrame(TEST_DF, subannual='01-01 00:00+01:00'))

    # assert that missing timezone fails
    assert not validate(IamDataFrame(TEST_DF, subannual='01-01 00:00'))

    # assert that wrong timezone fails
    assert not validate(IamDataFrame(TEST_DF, subannual='01-01 00:00+02:00'))

    # assert that value not castable to datetime fails
    assert not validate(IamDataFrame(TEST_DF, subannual='01-32 00:00+01:00'))


def test_validate_time_entry():
    df_sub = TEST_DF.rename(columns={'year': 'subannual'}).\
        replace([2005, 2010], value=['2005-06-17 00:00+01:00',
                                     '2010-07-21 12:00+01:00'])
    assert validate(IamDataFrame(df_sub))
