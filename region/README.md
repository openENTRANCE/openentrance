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

See [aggregate-regions.yaml](aggregate-regions.yaml) for the codelist.

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
and a mapping of ISO2-codes (including alternatives)
to the common country names.

```python
# load countries codelist from file
import yaml
with open('countries.yaml', 'r') as stream:
    country_codelist = yaml.load(stream, Loader=yaml.FullLoader)

# translate codelist to list and mapping (dictionary)
list_of_countries = list(country_codelist)
iso2_mapping = dict(
    [(country_codelist[c]['iso2'], c) for c in country_codelist]
    # add alternative iso2 codes used by the European Commission to the mapping
    + [(country_codelist[c]['iso2_alt'], c) for c in country_codelist
       if 'iso2_alt' in country_codelist[c]]
)
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
along the NUTS classification from the NUTS-3 codelist, i.e.,

```
hierarchy = {
    <country>: {
        <nuts1>: {
            <nuts2>: [<list of nuts3>],
            ... },
        ... },
   ... },
}
```

```python
# load NUTS-3 codelist from file
import yaml
with open(f'nuts3.yaml', 'r') as stream:
    nuts3_codelist = yaml.load(stream, Loader=yaml.FullLoader)

# auxiliary function to add key-value to object and return
def add_to(mapping, key, value):
    if key not in mapping:
        mapping[key] = value
    elif isinstance(value, list):
        mapping[key] += value
    return mapping[key]

hierarchy = dict()

# iterate over NUTS-3 codelist and recursively add items to the hierarchy dict
for n3, mapping in nuts3_codelist.items():
    country, n1, n2 = mapping['country'], mapping['nuts1'], mapping['nuts2']
    country_dict = add_to(hierarchy, country, {n1: dict()})
    n1_dict = add_to(country_dict, n1, {n2: list()})
    add_to(n1_dict, n2, [n3])
```

### Other sub-country area classification
=======

Other sub-country disaggregations, provided that they can be described as aggregations of NUTS1,2 or 3 regions, example:
- ehighway2050 clusters : we have a definition of each cluster as an aggregation of a list of NUTS3 regions
- agregation of ehighway2050 clusters such as:
Northern Italy = 52_IT + 53_IT
Southern Italy = 54_IT+55_IT+56_IT+98_IT
with Northern Italy + Southern Italy = IT


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

## Parallel connections of directional data

When timeseries data represents flows or capacity on one of several parallel
connections between regions (e.g., power lines, natural gas pipelines), the
convention above is not sufficient. For such cases, the convention for 
directional data can be extended with a `|` character 
(without spaces before/after).

> Norway>Germany|E54
