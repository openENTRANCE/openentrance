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
is "Year". Its `duration` attribute is set to`1`.

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

### Days and hour data

The ISO 8601 datetime format is adopted to consider the following levels: year, month, day, hour, minute, second, and time zone.

#### Example of this format:

Date plus hours and minutes:
      YYYY-MM-DDThh:mmTZD (eg 1997-07-16T19:20+01:00)
Date plus hours, minutes and seconds:
      YYYY-MM-DDThh:mm:ssTZD (eg 1997-07-16T19:20:30+01:00)
Date plus hours, minutes, seconds and a decimal fraction of a second
      YYYY-MM-DDThh:mm:ss.sTZD (eg 1997-07-16T19:20:30.45+01:00)

More details about the format could be found in [Date and Time Formats](https://www.w3.org/TR/NOTE-datetime).

#### Example for using this format:

The code snippet (Python) below shows how to transform different datetime formats to ISO 8601.

Local to ISO 8601:
```python
import datetime
datetime.datetime.now().isoformat()
>>> 2020-03-20T14:28:23.382748
```

UTC to ISO 8601:
```python
import datetime
datetime.datetime.now().isoformat()
>>> 2020-03-20T14:28:23.382748
```

Local to ISO 8601 with time zone information:
```python
import datetime
datetime.datetime.now().astimezone().isoformat()
>>> 2020-03-20T14:32:16.458361+13:00
```

UTC to ISO 8601 with time zone information:
```python
import datetime
datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
>>> 2020-03-20T01:31:12.467113+00:00
```

### Other categories

*Other categories to be added over time*
