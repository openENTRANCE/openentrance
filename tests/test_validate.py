from pathlib import Path
import pandas as pd
from pyam import IamDataFrame
import pytest

import sys

# this is necessary to make tests pass on GitHub Actions
sys.path.append(str(Path(__file__).parents[1]))
from workflow import main as workflow


TEST_DATA = pd.DataFrame(
    [
        ["model_a", "scen_a", "Europe", "Primary Energy", "EJ/yr", 1, 6.0],
    ],
    columns=["model", "scenario", "region", "variable", "unit", 2005, 2010],
)
TEST_DF = IamDataFrame(TEST_DATA)


def validate(df):
    try:
        workflow(df)
        return True
    except ValueError as e:
        print(e)
        return False


def test_validate():
    # test simple validation
    assert validate(TEST_DF)


def test_validate_fail():
    # test that simple validation fails on variable and region dimension
    print(validate(TEST_DF.rename(variable={"Primary Energy": "foo"})))

    assert not validate(TEST_DF.rename(variable={"Primary Energy": "foo"}))
    assert not validate(TEST_DF.rename(region={"Europe": "foo"}))


def test_validate_directional():
    # test that validation works as expected with directional data
    assert validate(TEST_DF.rename(region={"Europe": "Austria>Germany"}))
    assert not validate(TEST_DF.rename(region={"Europe": "Austria>foo"}))

    # test that directional data with more than one `>` fails
    assert not validate(TEST_DF.rename(region={"Europe": "Austria>Italy>France"}))


def test_validate_subannual_months():
    # test that validation works as expected with months
    # (and representative timeslices generally)
    assert validate(IamDataFrame(TEST_DATA, subannual="January"))
    assert not validate(IamDataFrame(TEST_DATA, subannual="foo"))


@pytest.mark.parametrize(
    "subannual, status",
    [
        ("01-01 00:00+01:00", True),
        ("01-01 00:00", False),
        ("01-01 00:00+02:00", False),
        ("01-32 00:00+01:00", False),
    ],
)
def test_validate_subannual_datetime(subannual, status):
    # test that validation works as expected with continuous time as subannual
    assert validate(IamDataFrame(TEST_DATA, subannual=subannual)) == status


@pytest.mark.parametrize(
    "rename_mapping, status",
    [
        ({2005: "2005-06-17 00:00+01:00", 2010: "2010-06-17 00:00+01:00"}, True),
        ({2005: "2005-06-17 00:00+02:00", 2010: "2010-06-17 00:00+02:00"}, False),
        ({2005: "2005-06-17 00:00", 2010: "2010-06-17 00:00"}, False),
    ],
)
def test_validate_time_entry(rename_mapping, status):
    # test that validation works as expected with datetime-domain
    _df = IamDataFrame(
        IamDataFrame(TEST_DATA)
        .data.rename(columns={"year": "time"})
        .replace(rename_mapping)
    )
    assert validate(_df) == status


def test_validate_unit_entry():
    assert not (validate(df.rename(unit={"EJ/yr": "MWh"})))
