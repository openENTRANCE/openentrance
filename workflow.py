from pathlib import Path
import logging
import pyam
from nomenclature import DataStructureDefinition, RegionProcessor, process

here = Path(__file__).absolute().parent
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
from datetime import datetime, timedelta


# datetime must be in Central European Time (CET)
EXP_TZ = "UTC+01:00"
EXP_TIME_OFFSET = timedelta(seconds=3600)
OE_SUBANNUAL_FORMAT = lambda x: x.strftime("%m-%d %H:%M%z").replace("+0100", "+01:00")


def ecemf(df: pyam.IamDataFrame) -> pyam.IamDataFrame:
    """Entrypoint for ECEMF scenario validation"""
    return main(df, dimensions=["scenario", "region", "variable"])


def main(df: pyam.IamDataFrame, dimensions=["region", "variable"]) -> pyam.IamDataFrame:
    """Main function for validation and processing"""
    if "subannual" in df.dimensions or df.time_col == "time":
        dsd_dimensions = dimensions + ["subannual"]
    else:
        dsd_dimensions = dimensions

    # import definitions and region-processor
    definition = DataStructureDefinition(
        here / "definitions", dimensions=dsd_dimensions
    )
    processor = RegionProcessor.from_directory(here / "mappings", definition)

    # check if directional data exists in the scenario data, add to region codelist
    if any([r for r in df.region if ">" in r]):
        for r in df.region:
            if r in definition.region:
                continue
            r_split = r.split(">")
            if len(r_split) > 2:
                raise ValueError(
                    f"Directional data other than `origin>destination` not allowed: {r}"
                )
            elif len(r_split) == 2:
                if all([_r in definition.region for _r in r_split]):
                    # add the directional-region to the codelist (without attributes)
                    definition.region[r] = None

    # validate the region and variable dimensions, apply region processing
    df = process(df, definition, dimensions=dimensions, processor=processor)

    # convert to subannual format if data provided in datetime format
    if df.time_col == "time":
        logger.info('Re-casting from "time" column to categorical "subannual" format')
        df = df.swap_time_for_year(subannual=OE_SUBANNUAL_FORMAT)

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
