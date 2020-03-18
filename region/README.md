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

See [countries.yaml](countries.yaml) for the codelist.

#### Example for using this codelist

The code snippet (Python) below shows how to obtain the list of countries
and a mapping of ISO2-codes to the common country names.

```python
import yaml
with open('countries.yaml', 'r') as stream:
    country_mapping = yaml.load(stream, Loader=yaml.FullLoader)

list_of_countries = list(country_mapping.keys())
iso2_mapping = dict([(country_mapping[c]['iso2'], c)
                     for c in country_mapping.keys()])
```

### Sub-country areas

The disaggregation of countries follow the 
[NUTS 2021 classification](https://ec.europa.eu/eurostat/web/nuts/background)
used by Eurostat.

*To be added at a later stage*

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
