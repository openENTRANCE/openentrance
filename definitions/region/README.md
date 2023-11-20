# Guidelines for region names

The **region** column in the data format specifies the spatial scope
of the timeseries data.

## Levels of regions

The list of regions is grouped into several levels of spatial detail.

### Aggregate regions

This list covers groupings of several countries, like 'World', various
definitions of Europe and the EU, and other groupings of several countries
(e.g., [EFTA](https://en.wikipedia.org/wiki/European_Free_Trade_Association)).

*The definitions of regions chosen for this project are guided by energy*
*modelling conventions and pragmatism rather than political considerations.*

Given that models often have different regional scope or aggregation levels,
the convention chosen in this nomenclature allows a flexible use
of the terms `Europe` and `European Union`:
the codelist defines several alternative versions of these regions named
`Europe (*)` and `EU*`, respectively.

Each model should (if applicable) report data at the generic region name
and specify in the model documentation which definition was used.
If multiple definitions are possible, the model should use a specification
earlier in the codelist.

For example, if Turkey is a separate region in a model, the scenario results
for `Europe` should use definition `Europe (excl. Turkey)`
(from line 12 rather than 15)
and additionally report alternative region aggregation levels
using the specific name `Europe (incl. Turkey)` (if relevant).

### Countries

Each country in this list includes the ISO2 and ISO3 codes as an attribute
as well as a flag on EU membership and (optional) a list of synonyms.
The list also includes the alternatives to the *ISO 3166-1 alpha-2 standard*
used by the [European Commission](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
(`iso2_alt`).

See [countries.yaml](countries.yaml) for the codelist.
The source data and script to generate the codelist are available
in the [data](data) folder.

#### Example for using this codelist

The code snippet (Python) below shows how to obtain the list of countries
and a mapping of ISO2/3-codes (including alternatives)
to the common country names using the installable Python package.

```python
>>> import nomenclature as nc
>>> list(nc.countries)
['Albania', 'Andorra', 'Austria', ..., 'United Kingdom']
>>> nc.iso_mapping['GR']
'Greece'
>>> nc.iso_mapping['GRC']
'Greece'
>>> nc.iso_mapping['EL']
'Greece'
```

### Sub-country areas following the 'Nomenclature of Territorial Units for Statistics' (NUTS)

One set of disaggregation of countries follows the
[NUTS 2021 classification](https://ec.europa.eu/eurostat/web/nuts/background)
used by Eurostat.
 - Major socio-economic regions: [nuts1.yaml](nuts1.yaml)
 - Basic regions for the application of regional policies: [nuts2.yaml](nuts2.yaml)
 - Small regions for specific diagnoses: [nuts3.yaml](nuts3.yaml)

Each file includes the mapping of the NUTS-x code to the country name
(as defined in [countries.yaml](countries.yaml))
and the "parent" region(s) for NUTS-2 and NUTS-3 areas.

The script to generate the codelist is available in the [data](data) folder.
The source file `NUTS2016-NUTS2021.xlsx` can be downloaded from the
[NUTS 2021 classification](https://ec.europa.eu/eurostat/web/nuts/background)
website (last download March 27, 2020, per [@erikfilias](https://github.com/erikfilias)).

#### Example for using this codelist

The code snippet (Python) below shows how to obtain a recursive dictionary
along the NUTS classification, i.e.,

```
nuts_hierarchy = {
    <country>: {
        <nuts1>: {
            <nuts2>: [<list of nuts3 areas>],
            ... },
        ... },
   ... },
}
```

The package also includes a `regions` dictionary with the names
of all NUTS areas.

```python
>>> import nomenclature as nc
>>> nc.nuts_hierarchy['Belgium']['BE2']['BE24']
['BE241', 'BE242']]
>>> nc.regions['BE241']['name']
'Arr. Halle-Vilvoorde'
```

### Other sub-national area classification

Other sub-national disaggregations can be defined, ideally described as aggregations
of NUTS1,2 or 3 regions.

#### ehighway2050 clusters

**e-highway2050** was an EU-funded project (2012-2015), whose objective was to provide a
modular and robust expansion plan for the Pan-European Transmission Network from 2020
to 2050.

It defined a cluster model of the Pan-European transmission grid (D2.2),
see https://docs.entsoe.eu/baltic-conf/bites/www.e-highway2050.eu/e-highway2050/.

The cluster model is included in the definitions, see [ehighway.yaml](ehighway.yaml).

### Classification at a more detailed level (municipality, district, etc.)

*To be added at a later stage*

## Directional timeseries data

To represent data that refers to a flow or capacity between regions,
any two regions names **at the same level of spatial detail** can be
combined using a `>` character (without spaces before/after that character).

Bi-directional data must be declared separately for each direction using only
the `>` character. No other characters (`<>`, `=`) are allowed to
represent directional data.

Example:

> Norway>Germany

To represent data that refers to a flow or cost contribution of a generator
or a demand in a region to a connection between two regions, the name of the region
of the contributing agent (generator or demand) can be combined with the bi-directional data using 
a `:` character before the bi-directional data (without spaces before/after that character).

The region of the contributing agent can be of **a different level of spatial detail**
from the two regions specified in the bi-directional data.

Example:

> DE30:France>Spain

## Parallel connections of directional data

When timeseries data represents flows or capacity on one of several parallel
connections between regions (e.g., power lines, natural gas pipelines), the
convention above is not sufficient. For such cases, the convention for
directional data can be extended with a `|` character
(without spaces before/after).

> Norway>Germany|E54
