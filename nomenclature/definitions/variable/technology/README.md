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

- `Capacity|<Fuel>`
- `Capacity|<Fuel>|<Specification>`
- `Capacity|<Fuel>|<Specification>|<Identifier Of A Specific Power Plant>`

## Capital Cost

Variables for the overnight capital cost for new construction of power plants
or tranmission lines should follow the structure below.

- `Capital Cost|<Fuel>|<Specification>`
- `Capital Cost|<Fuel>|<Specification>|<Identifier Of A Specific Power Plant>`

Note that it usually does not make sense to report capital costs
at a more aggregate level (i.e., `Capital Cost|<Fuel>`).

## Investment expenditure

Variables for the expenditure for new construction of power plants
or tranmission lines should follow the structure below.

- `Investment|<Type>`
- `Investment|<Type>|<Fuel>`
- `Investment|<Type>|<Fuel>|<Specification>`
