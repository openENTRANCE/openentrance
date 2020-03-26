from pathlib import Path
import pandas as pd

# read csv file
df = pd.read_csv('variables_iamc15.csv', header=None)

# print a list top-level categories in the file
cats = list(pd.Series([i.split('|')[0] for i in df[0]]).unique())
print('list of top-level categories:')
for c in cats:
    print(f'    {c}')
