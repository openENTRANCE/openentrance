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

### Daily and hourly data
Our convention makes reference to the following agreements:


#### UTC datetime format:
- Standard datetime format     : **UTC**  
> The UTC datetime format is adopted to consider the following levels: year, month, day, hour, minute, and second (without consider time zones).
> For example: `2020-01-01, 2020-01-02, ...` or `2020-01-01T13:00, ...`
> Inclusion of attributes is possible such as duration (More details [here](https://github.com/openENTRANCE/nomenclature/blob/master/nomenclature/definitions/subannual/months.yaml))

- Using time zone                    : **no relevance**


#### Using the format:

The code snippet (Python) below shows how to get lists of dates and datetimes.

- To get a list of dates:
```python
from datetime import timedelta, date

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

start_dt = date(2015, 12, 20)
end_dt = date(2016, 1, 11)
for dt in daterange(start_dt, end_dt):
    print(dt.strftime("%Y-%m-%d"))
```
- To get a list of datetimes:
```python
from datetime import timedelta, datetime

def DateTimeRange(datetime1, datetime2):
    for n in range(int (((datetime2 - datetime1).days)+1)*24):
        yield datetime1 + timedelta(hours=n)

start_dt = datetime(2020, 6, 23)
end_dt   = datetime(2020, 6, 30)
for dt in DateTimeRange(start_dt, end_dt):
    print(dt.strftime("%Y-%m-%d %H:%M:%S"))
```

The format `"%Y-%m-%d %H:%M:%S"` is composed by tokens. Each token represents a different part of the date-time, like day, month, year, etc. More details can be found in [strftime() and strptime() section](https://docs.python.org/3/library/datetime.html).
For a quick reference, here is what we're using in the code above:

- %Y: Year (4 digits)
- %m: Month
- %d: Day of month
- %H: Hour (24 hour)
- %M: Minutes
- %S: Seconds

*Other categories to be added over time*
