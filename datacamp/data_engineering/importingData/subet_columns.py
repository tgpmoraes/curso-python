import pandas as pd

file_path = 'Streamlined-Data-Ingestion-with-pandas-Datacamp-main'

# Create list of columns to use
cols = ['zipcode', 'agi_stub', 'mars1', 'MARS2', 'NUMDEP']

# Create data frame from csv using only selected columns
data = pd.read_csv(f'../{file_path}/vt_tax_data_2016.csv',
                   usecols=cols,
                   nrows=500)

# View counts of dependents and tax returns by income level
print(data.groupby("agi_stub").sum())
