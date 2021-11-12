# Guidelines for variable definitions

The **variable** column specifies which type of information is provided in
the specific timeseries. This can be for example quantities of energy, prices,
economic activity, or specifications of technology parameters.

## Overview

### The variable hierarchy

This column implements a "semi-hierarchical" structure using the `|` character
(pipe, not l or i) to indicate the *depth*.
Semi-hierarchical means that a hierarchy can be imposed,
e.g., a user can enforce that the sum of `Emissions|CO2|Energy` and
`Emissions|CO2|Other` must be equal to `Emissions|CO2`
(if there are no other `Emissions|CO2|…` variables).
However, this is not mandatory, e.g., the sum of `Primary Energy|Coal`,
`Primary Energy|Gas`, `Primary Energy|Fossil` and other `Primary Energy|…`
data should not be expected to equal `Primary Energy`
because this would double-count fossil fuels.

### Naming convention for variables

When suggesting/adding new variables, please follow these rules:

- A `|` (pipe) character indicates levels of hierarchy
- Do not use spaces before and after the `|` character,
  but add a space between words (e.g., `Primary Energy|Non-Biomass Renewables`)
- All words must be capitalised (except for 'and', 'w/', 'w/o', etc.)
- Do not use abbreviations (e.g, 'PHEV') unless strictly necessary
- Add hierarchy levels where it might be useful in the future, e.g., use 
  `Electric Vehicle|Plugin-Hybrid` instead of 'Plugin-Hybrid Electric Vehicle'
- Do not use abbreviations of statistical operations ('min', 'max', 'avg')
  but always spell out the word
- Do not include words like 'Level' or 'Quantity' in the variable,
  because this should be clear from the context

### Common terms

Variables are usually constructed with a top-level category/indicator
(e.g, `Primary Energy`, `Capacity`)
followed by a number of categories and specification
(e.g., `<Fuels>`, `<Sectors>`).
Examples for common values used to construct variables are given below.
These are not intended to be hierarchical or mutually exclusive;
instead, it is the responsibility of the modelling team to choose
an appropriate subset of variables in their reporting workflows.

- Fuels: `Fossil`, `Coal`, `Oil`, `Gas`, `Nuclear`,
  `Non-Biomass Renewables`, `Hydro`, `Solar`, `PV`, `Biomass`,
  `Electricity`<sup>[1]</sup>, `Heat`, ...
- Sectors: `Industry`, `Residential and Commercial`, `Transportation`,
  `Non-Energy Use`, ...
- Specifications: `Offshore`, `Onshore`, `w/ CCS`, `w/o CCS`,`Freight`, ...

[1] Please use `Electricity` instead of `Power` for consistency
(except for "power plant") 

## Categories of variables

This section provides an overview of the top-level categories or indicators
of the variable dimension, i.e., `<Category>|...`.
The detailed explanation and codelists are provided in the subfolders.

### Production, generation and consumption of energy (fuels)

This category includes three top-level indicators related to the energy supply
chain (also called reference energy system):

- `Primary Energy`
- `Secondary Energy`
- `Final Energy`

[More information](../variable/energy)

### Characteristics of (energy) technologies

This section defines variables and indicators related to characteristics and
specifications of (energy) technologies including power plants, transmission
lines and pipelines.

- `Capacity`
- `Capital Cost`
- `Investment`

[More information](../variable/technology)

### Emissions, carbon sequestration and climate

This section defines variables and indicators related to emissions,
carbon sequestration and the impact of emissions on the climate
(i.e., temperature).

- `Emissions`
- `Carbon Sequestration`
- `Temperature`

[More information](../variable/emissions)

### Macro-economic indicators and societal drivers

This section defines variables and indicators related to the economy
and societal drivers such as population.

- `Discount Rate`
- `Population`
- `GDP`
- `Consumption`
- `Price`
- `Policy Cost`

[More information](economy)

## Definition of units

The list of variables (codelists) defined in the `yaml`-files in the subfolders
contain an attribute `unit`, which specifies the recommended unit for
this indicator.

*It is currently still under discussion whether the recommended unit
should be interpreted as mandatory.*

For unit conversion as part of the pre- or postprocessing in the model workflow,
the Python package **pyam** provides an intuitive and low-level interface;
see [this tutorial](https://pyam-iamc.readthedocs.io/en/stable/tutorials/unit_conversion.html)
for more information.
