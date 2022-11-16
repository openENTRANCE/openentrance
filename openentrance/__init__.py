from pathlib import Path

from nomenclature.codelist import RegionCodeList


# path to nomenclature definitions
DEF_PATH = Path(__file__).parent.parent / "definitions" / "region"


countries = RegionCodeList.from_directory(
    "region", path=DEF_PATH, file_glob_pattern="countries.yaml"
)
"""CodeList of countries"""

iso_mapping = dict(
    [(countries[c].iso3, c) for c in countries]
    + [(countries[c].iso2, c) for c in countries]
    # add alternative iso2 codes used by the European Commission to the mapping
    + [
        (countries[c].iso2_alt, c)
        for c in countries
        if hasattr(countries[c], "iso2_alt")
    ]
)
"""Dictionary of iso2/iso3/alternative-iso2 codes to country names"""


def _add_to(mapping, key, value):
    """Add key-value to mapping"""
    if key not in mapping:
        mapping[key] = value
    elif isinstance(value, list):
        mapping[key] += value
    return mapping[key]


def _create_nuts_hierarchy():
    """Parse nuts3.yaml and create hierarchical dictionary"""

    hierarchy = dict()
    nuts3 = RegionCodeList.from_directory(
        "region", path=DEF_PATH, file_glob_pattern="nuts3.yaml"
    )

    for n3, code in nuts3.items():
        country, n1, n2 = [getattr(code, i) for i in ["country", "nuts1", "nuts2"]]
        country_dict = _add_to(hierarchy, country, {n1: dict()})
        n1_dict = _add_to(country_dict, n1, {n2: list()})
        _add_to(n1_dict, n2, [n3])
    return hierarchy


nuts_hierarchy = _create_nuts_hierarchy()
"""Hierarchical dictionary of NUTS region classification"""
