import nomenclature

definition = nomenclature.DataStructureDefinition("definitions")


def test_variables():
    # check that regions dictionary is not empty and has specific element
    assert "Emissions|CO2" in definition.variable


def test_variables_fuel_types():
    # check that exploding of {Fuel} to fuels works (including CCS subcategory)
    obs = definition.variable["Secondary Energy|Electricity|Gas"]
    exp = (
        "Net electricity production from natural gas "
        "(including methane from biomass or hydrogenation)"
    )
    assert obs.description == exp

    obs = definition.variable["Secondary Energy|Electricity|Gas|w/ CCS"]
    exp = (
        "Net electricity production from natural gas (including methane "
        "from biomass or hydrogenation) with a CO2 capture component"
    )
    assert obs.description == exp


def test_variables_industry_types():
    # check that exploding of {industry} to industries works
    obs = definition.variable["Capital|iAGRI"]
    exp = "Total capital costs spend by agriculture"
    assert obs.description == exp


def test_variables_transport_mode():
    # check that exploding of {Transport mode} to transportation modes works
    obs = definition.variable["Energy Service|Transportation|Freight|Rail"]
    exp = "Provision of energy services related to freight " "rail-based transportation"
    assert obs.description == exp


def test_variables_product_types():
    # check that exploding of {product} to products works
    obs = definition.variable["Consumption|Households|pAGRI|Imported"]
    exp = "Consumption of imported agriculture by households"
    assert obs.description == exp


def test_regions():
    # check that regions dictionary is not empty and has specific element
    assert "Europe" in definition.region
