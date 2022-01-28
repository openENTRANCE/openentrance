# Production, generation and consumption of energy (fuels)

The variables relating to the production, generation and consumption of
energy fuels can be separated into three groups according to their position
along the supply chain or reference energy system.

## Primary Energy

This group includes extraction of fossil resources and production/generation
of energy/fuels from renewables. 
The hierarchy of variables in this group should follow this style:

- `Primary Energy`
- `Primary Energy|{Fuel}`
- `Primary Energy|{Fuel}|{Specification}`

See [energy-primary.yaml](energy-primary.yaml) for the full codelist.

## Secondary Energy

This group includes any fuel or energy carrier resulting from
an intermediate conversion process (e.g., electricity generation, gasoline).
The hierarchy of variables in this group should follow this style:

- `Secondary Energy|<Output Fuel>`
- `Secondary Energy|<Output Fuel>|<Input Fuel>`
- `Secondary Energy|<Output Fuel>|<Input Fuel>|{Specification}`

See [energy-secondary.yaml](energy-secondary.yaml) for the full codelist.

## Final Energy

This group includes any fuel or energy carrier at the point of consumption.
The sub-categories of this group can be separated into a by-source (eg type of fuel), 
a by-sector dimension (sector= users, eg industry, commercial, residential) 
and a by-uses dimension (uses=transportation, heating, industrial process...)

The hierarchy of variables in this group should follow this style:

- `Final Energy`
- `Final Energy|{Fuel}`
- `Final Energy|{Fuel}|{Specification}`
- `Final Energy|{Sector}`
- `Final Energy|{Sector}|{Specification}`
- `Final Energy|{Sector}|{Fuel}|{Specification}`

To avoid overlap of variable definitions, data reported at the level
of sector *and* fuel, the variable should follow the convention
`Final Energy|{Sector}|{Fuel}|{Specification}`
(not `Final Energy|{Fuel}|{Sector}|{Specification}`).

See [energy-final.yaml](energy-final.yaml) for the full codelist.
