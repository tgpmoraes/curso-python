import os
import pandas as pd


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\python_programer\\data_types'
os.chdir(data_dir)

records = pd.read_csv('baby_names.csv')

baby_names_2014 = set(records[records['BRITH_YEAR'] == 2014]
                             ['NAME'].str.capitalize())

records = records.values.tolist()

# Create the empty set: baby_names_2011
baby_names_2011 = set()

# Loop over records and add the names from 2011 to the baby_names_2011 set
for row in records:
    # Check if the first column is '2011'
    if row[0] == 2011:
        # Add the fourth column to the set
        baby_names_2011.add(row[3].capitalize())

# Find the difference between 2011 and 2014: differences
differences = baby_names_2011.difference(baby_names_2014)

# Print the differences
print(differences)
