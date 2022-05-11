from pathlib import Path
import pandas as pd

this = Path(__file__).name

# read csv file
countries = pd.read_csv("countries.csv", header=None)

# open file and write header
file = open("../countries.yaml", "w")
file.writelines(f"# This file was created using the script `data/{this}`\n")

file.write("# DO NOT ALTER THIS FILE MANUALLY!\n\n")
file.write("# List of countries\n")

file.write("- Countries:\n")

# the EU uses alternative ISO2 codes for some countries
iso2_alternatives = {"GB": "UK", "GR": "EL"}

# write list of countries with dictionary of relevant information
for i, (name, iso2, iso3, eu, syn) in countries.iterrows():
    file.write(f"  - {name}:\n")
    file.write(f"      eu_member: {'true' if eu is True else 'false'}\n")
    file.write(f"      iso2: {iso2}\n")
    if iso2 in iso2_alternatives.keys():
        file.write(f"      iso2_alt: {iso2_alternatives[iso2]}")
        file.write(" # the European Commission uses alternative ISO2 codes\n")
    file.write(f"      iso3: {iso3}\n")
    if isinstance(syn, str):
        file.write(f"      synonyms: {syn}\n")

# close file
file.close()
