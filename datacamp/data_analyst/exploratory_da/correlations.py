import os
import pandas as pd


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\exploratory_da\\data'
os.chdir(data_dir)

brfss = pd.read_hdf('brfss.hdf5')

# Select columns
columns = ['AGE', 'INCOME2', '_VEGESU1']
subset = brfss[columns]

# Compute the correlation matrix
print(subset.corr())
