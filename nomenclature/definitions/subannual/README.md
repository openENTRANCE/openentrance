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


#### Examples for using this format:

The code snippet (Python) below shows how to use the datetime format.

```python
import datetime

dt_str = '2018-06-29 08:15:00'
dt_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')

print('Date:', dt_obj.date())
print('Time:', dt_obj.time())
print('Date-time:', dt_obj)
>>> Date: 2018-06-29
>>> Time: 08:15:00
>>> Date-time: 2018-06-29 08:15:00
```

The format `"%Y-%m-%d %H:%M:%S"` is composed by tokens. Each token represents a different part of the date-time, like day, month, year, etc. More details can be found in [strftime() and strptime() section](https://docs.python.org/3/library/datetime.html).
For a quick reference, here is what we're using in the code above:

%Y: Year (4 digits)
%m: Month
%d: Day of month
%H: Hour (24 hour)
%M: Minutes
%S: Seconds

### Representatives of time-slices

- Using winter/summer time   :
> To distinguish between different granularity levels of representative timeslices, It was proposed the following: `<Granularity>|<Name of timeslice>`. For example: `2 Season-2 Times|Summer-Day`.

- Averaging values over the time span   :
> A value is always the average for flow variables (i.e. It is the average between the subannual time and the subsequent one, where average is contingent on the lowest level of granularity - if you use 2020-01-01T13:00, it is hourly average, if you use 2020-01-01, it is daily average...).
> Reference comment -> [here](https://github.com/openENTRANCE/nomenclature/issues/46#issuecomment-641721712)

- Accumulating values over the time span:
> A value at the start of the period for stock over the time-period until the start of the next timeslice.
> For example, Capacity or Reservoir Level at 2020-01-01T13:00 is the value at 1pm, if subannual is given as 2020-01-01, it is understood as midnight that day, if it's January, it is understood as midnight on the first day of the month.
> Reference comment -> [here](https://github.com/openENTRANCE/nomenclature/issues/46#issuecomment-641721712)

### Other categories

*Other categories to be added over time*
