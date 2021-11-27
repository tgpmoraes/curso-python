import os
import pandas as pd


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\python_programer\\data_types'
os.chdir(data_dir)

records = pd.read_csv('baby_names.csv')

baby_names_2011 = set(records[records['BRITH_YEAR'] == 2011]
                             ['NAME'].str.capitalize())

baby_names_2014 = set(records[records['BRITH_YEAR'] == 2014]
                             ['NAME'].str.capitalize())

# Find the union: all_names
all_names = baby_names_2011.union(baby_names_2014)

# Print the count of names in all_names
print(len(all_names))

# Find the intersection: overlapping_names
overlapping_names = baby_names_2011.intersection(baby_names_2014)

# Print the count of names in overlapping_names
print(len(overlapping_names))
