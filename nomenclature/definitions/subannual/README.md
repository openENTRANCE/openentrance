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
Timeslices can be either understood as consecutive periods or as
representative periods (e.g., "summer-day").

Each item in the codelists below includes an attribute `duration` indicating
the duration relative to a normal year (i.e., not a leap year).

### Yearly data

The default entry for the openENTRANCE data format in the "subannual" column
is "Year". Its `duratuon` attribute is set to`1`.

### Months

See [months.yaml](months.yaml) for the codelist.

#### Example for using this codelist

The code snippet (Python) below shows how to obtain a mapping of months
to their respective duration.

```python
import yaml
with open(f'../subannual/months.yaml', 'r') as stream:
    months = yaml.load(stream, Loader=yaml.FullLoader)

mapping = dict([(m, eval(attr['duration'])) for (m, attr) in months.items()])
```

### Other categories

*Other categories to be added over time*
