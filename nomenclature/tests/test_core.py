import nomenclature as nc


def test_variables():
    # check that regions dictionary is not empty and has specific element
    assert 'Emissions|CO2' in nc.variables


def test_variables_fuel_types():
    # check that exploding of <Fuel> to fuels works (including CCS subcategory)
    obs = nc.variables['Secondary Energy|Electricity|Gas']
    exp = 'Net electricity production from natural gas ' \
          '(including methane from biomass or hydrogenation)'
    assert obs['description'] == exp

    obs = nc.variables['Secondary Energy|Electricity|Gas|w/ CCS']
    exp = 'Net electricity production from natural gas (including methane ' \
          'from biomass or hydrogenation) with a CO2 capture component'
    assert obs['description'] == exp


def test_variables_industry_types():
    # check that exploding of <industry> to industries works
    obs = nc.variables['Capital|iAGRI']
    exp = 'Total capital costs spend by agriculture'
    assert obs['description'] == exp


def test_variables_transport_types():
    # check that exploding of <transport> to transportation modes works
    obs = nc.variables['Energy Service|Transportation|Freight|Rail']
    exp = 'Provision of energy services related to freight ' \
          'rail-based transportation technologies'
    assert obs['description'] == exp


def test_variables_product_types():
    # check that exploding of <product> to procuts works
    obs = nc.variables['Consumption|Households|pAGRI|Imported']
    exp = 'Consumption of imported agriculture by households'
    assert obs['description'] == exp


def test_regions():
    # check that regions dictionary is not empty and has specific element
    assert 'Europe' in nc.regions


def test_iso_mapping():
    # check that iso-mapping dictionary is not empty and has specific elements
    for name in ['GR', 'GRC', 'EL']:
        assert nc.iso_mapping[name] == 'Greece'


def test_nuts_hierarchy():
    # check that nuts-hierarchy is not empty and has specific elements
    assert nc.nuts_hierarchy['Belgium']['BE2']['BE24'] == ['BE241', 'BE242']
