# Characteristics of (energy) technologies

This section defines variables and indicators related to characteristics and
specifications of (energy) technologies including power plants, transmission
lines and pipelines.

Note that there is no clear distinction whether a variable defined in this
section is an assumption (input) or a model result (output) - this depends
on the context of the modelling framework.
For example, the "installed capacity" of a power plant
may be an exogenous assumption in a (short-term) power-system dispatch model
or a result from a long-term investment model.
The respective use case should be clearly specified in the model documentation.

Explanations of the different categories and the structures
of the variables are given below.
See [technologies.yaml](technologies.yaml) for the full codelist.

## Installed Capacity

Variables for the installed capacity of (energy) production/generation
or transmission should follow the structure below.

- `Capacity|{Fuel}`
- `Capacity|{Fuel}|{Specification}`
- `Capacity|{Fuel}|{Specification}|{Identifier Of A Specific Power Plant}`

## Capital Cost

Variables for the overnight capital cost for new construction of power plants
or tranmission lines should follow the structure below.

- `Capital Cost|{Fuel}|{Specification}`
- `Capital Cost|{Fuel}|{Specification}|{Identifier Of A Specific Power Plant}`

Note that it usually does not make sense to report capital costs
at a more aggregate level (i.e., `Capital Cost|{Fuel}`).

## Investment expenditure (outdated/ superseded by investment variables split by sector - see below)

Variables for the expenditure for new construction of power plants
or tranmission lines should follow the structure below.

- `Investment|{Type}`
- `Investment|{Type}|{Fuel}`
- `Investment|{Type}|{Fuel}|{Specification}`

## Investment expenditures - Energy supply/demand sectors

Variables for the investment expenditure in an energy (sub-)sectors (currently {Residential/Commercial}, Transportation, Industry, Electricity, Extraction, Heat, Hydrogen, and Liquids). Examples are 

- `Investment|Energy Demand|Transportation`
- `Investment|Energy Demand|{Residential/Commercial}`
- `Investment|Energy Demand|{Residential/Commercial}|Appliances`
- `Investment|Energy Demand|{Residential/Commercial}|Heating and Cooling|Heat Pumps`
- `Investment|Energy Supply|Electricity|{Electricity Input}`
- `Investment|Energy Supply|Extraction|Oil`
- `Investment|Energy Supply|Liquids|Biomass`

## Annualized Investments - Energy supply/demand sectors

Annualized investments of the standing stock. This includes the annualized investments for all the currently standing stock that is not yet financially depreciated (which can happen earlier than the technical lifetime). The sum over the annualized investment should - over long periods that are longer than the depreciation periods - come close to the sum over investments; but it will be different on short periods if large investments are undertaken to change the system, which will strongly increase the "Investment" variable but have less impact on the "Annualized Investment" variable, which also includes the contribution for the standing stock. Towards the end of the modeling period, the annualized investment approach can give a better impression of the costs for the remaining years until end of the modelling period; the "Investment" variable also contains the investments whose lifetime lies mostly after the end of the modelling period. Example

- `Annualized Investment|Energy Demand|{Residential/Commercial}`
- `Annualized Investment|Energy Demand|Transportation|{Transport mode}`

## Running Costs - Energy supply/demand sectors

Variables for the running costs of a sector, eg {Residential/Commercial}, Transportation, Industry, Electricity, Hydrogen. Currently implemented subtypes are "Operation and Maintenance", as well as "Fuel"

- `Running Costs|Energy Demand|{Residential/Commercial}` 
- `Running Costs|Energy Demand|Transportation|{Transport mode}|Fuel` 
- `Running Costs|Energy Demand|Transportation|{Transport mode}|Fuel|{Fuel}`
- `Running Costs|Energy Demand|Industry|Operation and Maintenance`

## Stock and Sales of technologies within a sector

- `Stock|Transportation|{Transport mode, tech and carrier}` 
- `Sales|{Residential/Commercial}|Heat Pumps`