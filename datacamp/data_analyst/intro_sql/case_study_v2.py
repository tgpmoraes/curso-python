# Import create_engine, MetaData
from sqlalchemy import create_engine, MetaData, Table, insert
import os
import pandas as pd


def append_row(values_list, row):
    data = {'state': row.state, 'sex': row.sex,
            'age': row.age, 'pop2000': row.pop2000,
            'pop2008': row.pop2008}
    values_list.append(data)


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\intro_sql'
os.chdir(data_dir)

# Define an engine to connect to chapter5.sqlite: engine
engine = create_engine('sqlite:///chapter5.sqlite')

# Create a connection on engine
connection = engine.connect()

# Create a metadata object: metadata
metadata = MetaData()

# Reflect census table via engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Initialize MetaData: metadata
metadata = MetaData()

csv_reader = pd.read_csv('census.csv', header=None)
csv_reader.columns = ['state', 'sex', 'age', 'pop2000', 'pop2008']

# Create an empty list: values_list
values_list = []

csv_reader.apply(lambda row: append_row(values_list, row), axis=1)

# Build insert statement: stmt
stmt = insert(census)

# Use values_list to insert data: results
results = connection.execute(stmt, values_list)

# Print rowcount
print(results.rowcount)
