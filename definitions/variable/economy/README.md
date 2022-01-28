# Macro-economic indicators and societal drivers

This section defines variables and indicators related to the economy
and societal drivers such as population.

Explanations of the different categories and the structures
of the variables are given below.
See [economy.yaml](economy.yaml) for the full codelist.

## Discount Rate

The discount rate should be distinguished by sector or (group of) firms
and follow the structure below.

- `Discount rate|{Sub-Category}`

For models assuming a social welfare maximization with a unique discount rate,
please use `Discount rate|Social`.  

## Population

The variables for population should follow the structure below.

- `Population`
- `Population|{Specification}`

Specifications can be linked to demographic characteristics (e.g., urban vs.
rural) or socio-economic aspects such as population at risk of hunger.

## Gross Domestic Product (GDP)

The variables for Gross Domestic Product (GDP) should follow the structure
below, where the method used for aggregation should be either
market-based exchange rates (MER) or purchasing-power parity (PPP).

- `GDP|{Method}`

## Consumption

The variable for total consumption (in monetary terms) currently does not
have any sub-categories or specification, but this could be added as required.

- `Consumption`

## Price

The variables for prices should follow the structure shown below.

As with other variables, it may depend on the context of the modelling
framework whether this timeseries is an assumption (input)
or a model result (output) -
see the section on variables related to [technologies](../../variable/technology)
for further discussion.

- `Price|Carbon`
- `Price|{Fuel}`
- `Price|{Fuel}|{Sector}`

## Policy Cost

The variables related to costs from policies (compared to a baseline)
should follow the structure below. The policies included in the metric and
the baseline used for comparison must be specified in the scenario protocol. 

- `Policy Cost|{Metric}`