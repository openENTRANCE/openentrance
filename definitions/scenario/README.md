# ECEMF project: Validation of scenario names

The ECEMF project enforces a list of valid scenario names. This list used to be
located in this folder, but was moved to https://github.com/iiasa/ecemf-workflow.

# openENTRANCE project: Guidelines for scenario names

The **scenario** column in the data format should use a simple name for the
pathway or case study analysis. It is recommended to use descriptive language
without abbreviations, unless they are intuitive to a general audience.

Scenario names should use capitalised terms separated by a space.
Names that specifically use work package or case study names are discouraged.

Example:

> Green Growth

## Versioning of the scenario protocol

If the scenario protocol (i.e., underlying assumptions or drivers) is changed
or there is a reasonable expectation that this may happen,
a version number using [semantic versioning](https://semver.org) can be added
to the scenario name.

> Green Growth 2.1

## Stochastic scenarios

If there are several realisations of a stochastic scenario, the convention
is that a `|` character should be used to separate the scenario name
from a meaningful indicator of the realisation (e.g, `High`, `Low`)
or a numbered list (e.g., `s001`).

> Green Growth 2.1|High Demand
