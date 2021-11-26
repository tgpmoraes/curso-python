# Import create_engine, MetaData, and Table
from sqlalchemy import (
    create_engine, Table, MetaData)
import os


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\intro_sql'
os.chdir(data_dir)

# Create an engine that connects to the census.sqlite file: engine
engine = create_engine('sqlite:///census_to_be_deleted.sqlite')

# Create a connection on engine
connection = engine.connect()

# Create a metadata object: metadata
metadata = MetaData()

# Reflect state_fact table from the engine: state_fact
state_fact = Table('state_fact', metadata, autoload=True, autoload_with=engine)

# Reflect census table via engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Drop the state_fact table
state_fact.drop(engine)

# Check to see if state_fact exists
print(state_fact.exists(engine))

# Drop all tables
metadata.drop_all(engine)

# Check to see if census exists
print(census.exists(engine))
