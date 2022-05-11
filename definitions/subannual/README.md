# Guidelines for subannual data resolution

The **subannual** column in the data format specifies the temporal scope
of the timeseries data at a sub-annual resolution.
The column is **not required**; if it is not provided,
the timeseries is understood as yearly data.
The default value for this column is 'Year'.

*This column is an extension compared to the format as defined by the
[IAMC](http://www.globalchange.umd.edu/iamc/) and used in the context
of IPCC Reports and other model comparison studies.
These previous scenario ensembles only used yearly timeseries data.*

## Overview

The list of subannual "timeslices" are grouped into several categories
and levels of temporal detail.
Timeslices can be either understood as consecutive (continuous) periods or as
representative periods (e.g., "summer-day").

Each item in the codelists below includes an attribute `duration` indicating
the duration relative to a normal year (i.e., not a leap year).

## Yearly data

The default entry for the openENTRANCE data format in the "subannual" column
is "Year". Its `duration` attribute is set to `1`.

## Continuous time formats with subannual resolution

### Months

See [months.yaml](months.yaml) for the codelist.

#### Example for using this codelist

The code snippet (Python) below shows how to obtain a mapping of months
to their respective duration.

```python
import yaml

with open(f"definitions/subannual/months.yaml", "r") as stream:
    months = yaml.safe_load(stream)

mapping = dict([(m, eval(attr['duration'])) for (m, attr) in months.items()])
```

### Daily or hourly resolution

We follow the datetime format (ISO 8601, see this overview
on [Wikipedia](https://en.wikipedia.org/wiki/ISO_8601)) to describe
continuous-time subannual resolution.

For consistency across the many models and tools in the consortium,
we use the format defined as `yyyy-mm-dd hh:mmz`,
where `z` specifies the timezone in the format `+hh:mm`.
For Python users, more details can be found in the documentation of the 
[datetime format](https://docs.python.org/3/library/datetime.html).

#### Time zone

Given the regional focus of this project, all hourly timestamps
must be given in Central European (standard) time
without consideration of daylight saving time (a.k.a. "summer time").

:warning: Any hourly timestamp must include the tag `z = '+01:00'`.

#### Calendar 

It is understood that continuous-time data follows the real calendar,
so that `2020-01-01` (January 1, 2020) is a Wednesday. Leap years must include
the data for February 29.

#### Time periods

It is understood that any value identified by a datetime timestamp
refers to the period **following that time** until the next given data point,
This means that if a model/scenario reports data at an hourly resolution,
the value associated with the timestamp `2020-01-01 00:00+01:00` refers
to the period from midnight until 1am.

#### Wide format vs. long format

The common openENTRANCE data format specifies that the "year" is separated
from the subannual timeslice identifier (wide format).
This can be implemented by specifying the "subannual" column
as `mm-dd hh:mmz` and setting the data column headers to `yyyy`.

| **model**   | **scenario**        | **region** | **variable**   | **unit** | **subannual**     | **2015** | **2020** | **2025** |
|-------------|---------------------|------------|----------------|----------|-------------------|---------:|---------:|---------:|
| GENeSYS-MOD | Societal Commitment | Europe     | Primary Energy | GJ/y     | 01-01 00:00+01:00 |     7.99 |     7.50 |      ... |
| ...         | ...                 | ...        | ...            | ...      | ...               |      ... |      ... |      ... |

Here, 7.99 GJ/yr is the amount of primary energy used in Europe
in the first hour of the year 2015.

Alternatively, one can represent the data with a "time" (in datetime format)
and a "value" column (long format). 

| **model**   | **scenario**        | **region** | **variable**   | **unit** | **time**               | **value** |
|-------------|---------------------|------------|----------------|----------|------------------------|---------:|
| GENeSYS-MOD | Societal Commitment | Europe     | Primary Energy | GJ/y     | 2015-01-01 00:00+01:00 |     7.99 |
| GENeSYS-MOD | Societal Commitment | Europe     | Primary Energy | GJ/y     | 2020-01-01 00:00+01:00 |     7.50 |
| ...         | ...                 | ...        | ...            | ...      | ...                    |      ... |

A (preliminary) utility function to translate from timeseries data
in `datetime` format (i.e., with columns `'time', 'value'`)
to `subannual + year` format
is available via `nomenclature.swap_time_for_subannual()`.

## Representative timeslices and other categories

*Other categories to be added over time*
