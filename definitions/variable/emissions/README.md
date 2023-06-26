# Emissions, carbon sequestration and climate

This section defines variables and indicators related to emissions,
carbon sequestration and the impact of emissions on the climate
(i.e., temperature).

## Emissions

Variables related to emissions should follow the structure below.

- `Emissions|{Species}`
- `Emissions|{Species}|{Specification}`

Examples of species: `CO2`, `CH4`, `CO`, `NOx`

## Carbon Sequestration

Carbon (dioxide) sequestered (stored) can be distinguished as several
subcategories:
 - Carbon Capture & Storage/Sequestration (CCS):
   carbon dioxide captured at the point of emission
   (energy sector & industrial processes)
 - Land Use: carbon dioxide sequestered through land-based sinks
 - Other methods: Direct Air Capture, Enhanced Weathering

Variables in this category should follow the structure below.

- `Carbon Sequestration|{Type}`
- `Carbon Sequestration|{Type}|{Specification}`

## Temperature

Variables in this category should follow the structure below.

- `Temperature|{Specification}`

## Codelist

See [emissions.yaml](emissions.yaml) for the full codelist.
