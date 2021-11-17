from openentrance import iso_mapping, nuts_hierarchy


def test_iso_mapping():
    # check that iso-mapping dictionary is not empty and has specific elements
    for name in ["GR", "GRC", "EL"]:
        assert iso_mapping[name] == "Greece"


def test_nuts_hierarchy():
    # check that nuts-hierarchy is not empty and has specific elements
    assert nuts_hierarchy["Belgium"]["BE2"]["BE24"] == ["BE241", "BE242"]
