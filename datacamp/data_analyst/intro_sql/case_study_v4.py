# Import create_engine, MetaData
from sqlalchemy import (create_engine, MetaData, Table, select, func,
                        case, cast, Float, desc)
import os


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

# Build a query to calculate the percentage of women in 2000: stmt
stmt = select([census.columns.state,
               (func.sum(
                   case([
                       (census.columns.sex == 'F', census.columns.pop2000)
                   ], else_=0)) /
                   cast(func.sum(census.columns.pop2000), Float) * 100)
               .label('percent_female')
               ])

# Group By state
stmt = stmt.group_by(census.columns.state)

# Execute the query and store the results: results
results = connection.execute(stmt).fetchall()

# Print the percentage
# for result in results:
#     print(result.state, result.percent_female)

# Build query to return state name and population difference from 2008 to 2000
stmt = select([census.columns.state,
               (census.columns.pop2008-census.columns.pop2000)
               .label('pop_change')
               ])

# Group by State
stmt = stmt.group_by(census.columns.state)

# Order by Population Change
stmt = stmt.order_by(desc('pop_change'))

# Limit to top 10
stmt = stmt.limit(10)

# Use connection to execute the statement and fetch all results
results = connection.execute(stmt).fetchall()

# Print the state and population change for each record
for result in results:
    print('{}:{}'.format(result.state, result.pop_change))
