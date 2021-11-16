from pathlib import Path

from nomenclature import CodeList


# path to nomenclature definitions
DEF_PATH = Path(__file__).parent.parent / "definitions"


countries = CodeList.from_directory(
    "region", path=DEF_PATH / "region", file="countries"
)
"""CodeList of countries"""

iso_mapping = dict(
    [(countries[c]["iso3"], c) for c in countries]
    + [(countries[c]["iso2"], c) for c in countries]
    # add alternative iso2 codes used by the European Commission to the mapping
    + [(countries[c]["iso2_alt"], c) for c in countries if "iso2_alt" in countries[c]]
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
    nuts3 = CodeList.from_directory("region", path=DEF_PATH / "region", file="nuts3")

    for n3, mapping in nuts3.items():
        country, n1, n2 = [mapping.get(i) for i in ["country", "nuts1", "nuts2"]]
        country_dict = _add_to(hierarchy, country, {n1: dict()})
        n1_dict = _add_to(country_dict, n1, {n2: list()})
        _add_to(n1_dict, n2, [n3])
    return hierarchy


nuts_hierarchy = _create_nuts_hierarchy()
"""Hierarchical dictionary of NUTS region classification"""
