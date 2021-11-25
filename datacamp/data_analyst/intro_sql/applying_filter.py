# Import create_engine function
from sqlalchemy import create_engine, Table, MetaData, select, and_
import os


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\intro_sql'
os.chdir(data_dir)

# Create an engine that connects to the census.sqlite file: engine
engine = create_engine('sqlite:///census.sqlite')

# Create an engine to the census database
# engine = create_engine(
#     'postgresql+psycopg2://' +
#     'student:datacamp' +
#     '@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com' +
#     ':5432/census')

# Create a connection on engine
connection = engine.connect()

# Create a metadata object: metadata
metadata = MetaData()

# Use the .table_names() method on the engine to print the table names
# print(engine.table_names())

# Reflect census table via engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Create a select query: stmt
stmt = select([census])

# Add a where clause to filter the results to only those
# for New York : stmt_filtered
stmt = stmt.where(census.columns.state == 'New York')

# Execute the query to retrieve all the data returned: results
results = connection.execute(stmt).fetchall()

# Loop over the results and print the age, sex, and pop2000
# for result in results:
#     print(result.age, result.sex, result.pop2000)

# Define a list of states for which we want results
states = ['New York', 'California', 'Texas']

# Append a where clause to match all the states in_ the list states
stmt = stmt.where(census.columns.state.in_(states))

# Loop over the ResultProxy and print the state and its population in 2000
# for result in connection.execute(stmt):
#     print(result.state, result.pop2000)

# Build a query for the census table: stmt
stmt = select([census])

# Append a where clause to select only non-male
# records from California using and_
stmt = stmt.where(
    # The state of California with a non-male sex
    and_(census.columns.state == 'California',
         census.columns.sex != 'M'
         )
)

# Loop over the ResultProxy printing the age and sex
for result in connection.execute(stmt):
    print(result.age, result.sex)
