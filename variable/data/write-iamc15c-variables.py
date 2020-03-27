from pathlib import Path
import pandas as pd

# read csv file
df = pd.read_csv('variables_iamc15.csv', header=None)

# print a list top-level categories in the file
cats = list(pd.Series([i.split('|')[0] for i in df[0]]).unique())
print('list of top-level categories:')
for c in cats:
    print(f'    {c}')

# specifications of the file to be generated
category_folder = '<folder>'
file_name = '<name>.yaml'
categories = ['<category>']
description = 'a short description'

# open file and write header
file = open(f'../{category_folder}/{file_name}', 'w')
this = Path(__file__).name
file.writelines(f'# This file was created using the script `data/{this}`\n')

file.write('# DO NOT ALTER THIS FILE MANUALLY!\n\n')
file.write(f'# List of variables related to {description}\n')

# loop over variable-description dataframe
for i, (variable, description, unit) in df.iterrows():

    # skip this variable if first level not in selected categories
    if not variable.split('|')[0] in categories:
        continue

    # clean-up of description text
    # (note that `:` is a reserved character in yaml-notation
    description = (
        (description[0].capitalize() + description[1:])
        .replace(':', ' -')
    )

    # write variable, description and unit
    file.write(f"\n{variable}:\n")
    # this if-then implements automated linebreaks in long descriptions
    if len(description) < 64:
        file.write(f'   description: {description}\n')
    else:
        d = description.split(' ')
        lst, i, f = [], 0, '   description: '
        for _d in d:
            if i + len(_d) > 63:
                file.write(f"{f}{' '.join(lst)}\n")
                lst, i, f = [], 0, ' ' * 16
            i += len(_d) + 1
            lst.append(_d)
        file.write(f"{f}{' '.join(lst)}\n")

    file.write(f"   unit: {unit}\n")

# close file
file.close()
