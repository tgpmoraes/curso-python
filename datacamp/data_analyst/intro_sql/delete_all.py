# Import create_engine, MetaData, and Table
from sqlalchemy import (
    create_engine, Table, MetaData, delete, select)
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

# Reflect census table from the engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Build a statement to empty the census table: stmt
delete_stmt = delete(census)

# Execute the statement: results
results = connection.execute(delete_stmt)

# Print affected rowcount
print(results.rowcount)

# Build a statement to select all records from the census table : select_stmt
select_stmt = select([census])

# Print the results of executing the statement to verify there are no rows
print(connection.execute(select_stmt).fetchall())
