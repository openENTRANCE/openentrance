# Guidelines for subannual data resolution

The **subannual** column in the data format specifies the temporal scope
of the timeseries data at a sub-annual resolution.
The column is **not required**; if it is not provided,
the timeseries is understood as yearly data.
The default value for this column is 'Year'.

*This column is an extension of the format as defined by the 
[IAMC](http://www.globalchange.umd.edu/iamc/) and used in the context
of IPCC Reports and other model comparison studies.
These previous scenario ensembles only used yearly timeseries data.*
