#  Project definitions for the openENTRANCE project

Copyright 2020-2024 openENTRANCE consortium

This repository is licensed under the Apache License, Version 2.0 (the "License"); see
the [LICENSE](LICENSE) for details.

[![license](https://img.shields.io/badge/License-Apache%202.0-black)](https://github.com/openENTRANCE/openentrance/blob/main/LICENSE)
[![python](https://img.shields.io/badge/python-3.7_|_3.8_|_3.9-blue?logo=python&logoColor=white)](https://github.com/openENTRANCE/openentrance)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## Aim and scope of this repository

<img src="./_static/open_entrance-logo.png" width="202" height="129" align="right" alt="openENTRANCE logo" />

The [Horizon 2020 openENTRANCE project](https://openentrance.eu) aims at
developing, using and disseminating an open, transparent and integrated
modelling platform for assessing low-carbon transition pathways in Europe.
A key requirement for an effective linking of models and consistent analysis is
a common "nomenclature", i.e., shared lists of variables, regions and units
used across the entire project.

This repository makes available the nomenclature used within the consortium and
serves as a discussion platform for extending the lists of terms.

*We invite other modelling teams to contribute and join the discussion,
hoping to facilitate increased cooperation across research projects
on (European) energy and climate policy!*

## How to work with this repository

There are several ways to interact with the nomenclature and definitions
provided in this repository. The simplest approach is to just read the `yaml`
files on GitHub - see the links [below](#Timeseries-data-dimensions).

The repository is structured so that it can be parsed by the
Python package **nomenclature** for scenario ensemble validation and processing.
Read more on [GitHub](https://github.com/iamconsortium/nomenclature)!

### An installable Python package

<img src="./_static/python.png" align="right" alt="Python logo" />

To facilitate using the definitions in data processing workflows and scripts,
there is an installable Python package with several utility
functions and dictionaries. [More information](openentrance)

## Data format structure

The openENTRANCE project uses a **common data format** based on a template
developed by the [Integrated Assessment Modeling Consortium (IAMC)](https://www.iamconsortium.org/)
and already in use in many model comparison projects at the global and national
level. While the IAMC comprises (mostly) integrated-assessment teams, the data
format is generic and can be used for a wide range of applications, including
energy-systems analysis or modelling of specific sectors like transport,
industry or the building stock.

### Timeseries data dimensions

In the data format, every timeseries is described by six dimensions (codes):

1.	Model - [more information](definitions/model)
2.	Scenario - [more information](definitions/scenario)
3.	Region - [more information](definitions/region)
4.	Variable - [more information](definitions/variable)
5.	Unit - see the section on [variables](definitions/variable)
    for details
6.	Subannual (optional, default 'Year')<sup>[1]</sup> -
    [more information](definitions/subannual)

In addition to these six dimensions, every timeseries is described by
a set of **year-value** pairs.

The resulting table can be either shown as
- **wide format** (see example below, with *years* as columns), or
- **long format** (two columns *year*  and *value*).

| **model**   | **scenario**        | **region** | **variable**   | **unit** | **subannual** | **2015** | **2020** | **2025** |
|-------------|---------------------|------------|----------------|----------|---------------|---------:|---------:|---------:|
| GENeSYS-MOD | Societal Commitment | Europe     | Primary Energy | EJ/y     | Year          |     69.9 |     65.7 |      ... |
| ...         | ...                 | ...        | ...            | ...      | ...           |      ... |      ... |      ... |

<sup>Data via the [IAMC 1.5°C scenario explorer](https://data.ene.iiasa.ac.at/iamc-1.5c-explorer),
    showing a scenario from the [CD-LINKS](https://www.cd-links.org) project.</sup>

[1] *The index 'Subannual' is an extension of the original format introduced by
the openENTRANCE project to accomodate data at a subannual temporal resolution.*

### Recommended usage of this data format

<img src="./_static/pyam-logo.png" width="133" height="100" align="right" alt="pyam logo" />

The Python package **pyam** was developed to facilitate working with timeseries
data conforming to this structure. Features include validation of values,
aggregation and downscaling of data, and import/export with various file formats
(`xlsx`, `csv`, ...) and table layouts (wide vs. long data).

[Read the docs](https://pyam-iamc.readthedocs.io) for more information!

## Funding acknowledgement

<img src="./_static/EU-logo-300x201.jpg" width="80" height="54" align="left" alt="EU logo" />
This project has received funding from the European Union’s Horizon 2020 research
and innovation programme under grant agreement No. 835896.
