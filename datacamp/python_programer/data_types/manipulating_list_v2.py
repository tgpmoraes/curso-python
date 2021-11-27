import os
import pandas as pd


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\python_programer\\data_types'
os.chdir(data_dir)

records = pd.read_csv('baby_names.csv')

records = records.values.tolist()

# Create the empty list: baby_names
baby_names = []

# Loop over records
for row in records:
    # Add the name to the list
    baby_names.append(row[3].lower())

# Sort the names in alphabetical order
for name in sorted(baby_names):
    # Print each name
    print(name)
