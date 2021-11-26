from sqlalchemy import create_engine, Table, MetaData, select
import pandas as pd
import os


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\intro_sql'
os.chdir(data_dir)

# Create an engine that connects to the census.sqlite file: engine
engine = create_engine('sqlite:///:memory:')

# Create a connection on engine
connection = engine.connect()

# Create a metadata object: metadata
metadata = MetaData()

# read census.csv into a DataFrame : census_df
census_df = pd.read_csv('census.csv', header=None)

# rename the columns of the census DataFrame
census_df.columns = ['state', 'sex', 'age', 'pop2000', 'pop2008']

# append the data from census_df to the "census" table via connection
census_df.to_sql(
    name='census', con=connection, if_exists='append', index=False)
