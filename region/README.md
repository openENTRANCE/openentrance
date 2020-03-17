# Guidelines for region names

The **region** column in the data format specifies the spatial scope
of the timeseries data.
The list of regions is grouped into several levels of spatial detail:

 - regions: World, various definitions of Europe and the EU,
   groupings of several countries
 - **countries**: see [countries.yaml](countries.yaml)
 - sub-country areas following the 
   [NUTS 2021 classification](https://ec.europa.eu/eurostat/web/nuts/background)
   used by Eurostat (which itself comprises three levels of spatial
   disaggregation)
 - classification at a more detailed level (municipality, district, etc.)

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
