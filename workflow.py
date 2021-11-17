from pathlib import Path
import logging
import pyam
from nomenclature import DataStructureDefinition

here = Path(__file__).absolute().parent
logger = logging.getLogger(__name__)
from datetime import datetime, timedelta


# datetime must be in Central European Time (CET)
EXP_TZ = "UTC+01:00"
EXP_TIME_OFFSET = timedelta(seconds=3600)


def main(df: pyam.IamDataFrame) -> pyam.IamDataFrame:
    """Main function for validation and processing"""
    logger.info("Starting openENTRANCE timeseries-upload processing workflow...")

    if "subannual" in df.dimensions:
        dimensions = ["region", "variable", "subannual"]
    else:
        dimensions = ["region", "variable"]

    definition = DataStructureDefinition(here / "definitions", dimensions=dimensions)

    definition.validate(df, dimensions=["region", "variable"])

    # convert to subannual format if data provided in datetime format
    if df.time_col == "time":
        logger.info('Re-casting from "time" column to categorical "subannual" format')
        df.swap_time_for_year(inplace=True)

    # check that any datetime-like items in "subannual" are valid datetime and UTC+01:00
    if "subannual" in df.dimensions:
        _datetime = [s for s in df.subannual if s not in definition.subannual]

        for d in _datetime:
            try:
                _dt = datetime.strptime(f"2020-{d}", "%Y-%m-%d %H:%M%z")
            except ValueError:
                try:
                    datetime.strptime(f"2020-{d}", "%Y-%m-%d %H:%M")
                except ValueError:
                    raise ValueError(f"Invalid subannual timeslice: {d}")

                raise ValueError(f"Missing timezone: {d}")

            # casting to datetime with timezone was successful
            if not (_dt.tzname() == EXP_TZ or _dt.utcoffset() == EXP_TIME_OFFSET):
                raise ValueError(f"Invalid timezone: {d}")

    return df
