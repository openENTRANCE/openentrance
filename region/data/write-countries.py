from pathlib import Path
import pandas as pd

this = Path(__file__).name

# read csv file
countries = pd.read_csv('countries.csv', header=None)

# open file and write header
file = open('../countries.yaml', 'w')
file.writelines(f'# This file was created using the script `utils/{this}`\n')

file.write('# DO NOT ALTER THIS FILE MANUALLY!\n\n')
file.write('# List of countries\n')

# write list of countries with dictionary of relevant information
for i, (name, iso2, iso3, eu, syn) in countries.iterrows():
    file.write(f"\n{name}:\n")
    file.write(f"   iso2: '{iso2}'\n")
    file.write(f"   iso3: '{iso3}'\n")
    file.write(f"   eu_member: {eu if eu is True else False}\n")
    if isinstance(syn, str):
        file.write(f'   synonyms: {syn}\n')

# close file
file.close()
