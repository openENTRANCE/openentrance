from pathlib import Path
import logging
import pyam
from nomenclature import DataStructureDefinition

here = Path(__file__).absolute().parent
logger = logging.getLogger(__name__)


def main(df: pyam.IamDataFrame) -> pyam.IamDataFrame:
    """Main function for validation and processing"""
    logger.info("Starting openENTRANCE timeseries-upload processing workflow...")

    if "subannual" in df.dimensions:
        dimensions = ["region", "variable", "subannual"]
    else:
        dimensions = ["region", "variable"]

    definition = DataStructureDefinition(here / "definitions", dimensions=dimensions)
    definition.validate(df)

    if df.time_col == "time":
        logger.info('Re-casting from "time" column to categorical "subannual" format')
        df.swap_time_for_year(inplace=True)

    return df
