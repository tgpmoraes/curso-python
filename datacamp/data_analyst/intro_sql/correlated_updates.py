# Import Table, Column, String, Integer, Float, Boolean from sqlalchemy
from sqlalchemy import create_engine, Table, MetaData, select,\
    Table, Column, String, Integer, insert, update
import os


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\intro_sql'
os.chdir(data_dir)

# Create an engine that connects to the census.sqlite file: engine
engine = create_engine('sqlite:///census.sqlite')

# Create a connection on engine
connection = engine.connect()

# Create a metadata object: metadata
metadata = MetaData()

# Define a new table with a name, count, amount, and valid column: data
# flat_census = Table('flat_census', metadata,
#                     Column('state_name', String(255)),
#                     Column('fips_code', Integer(), default=1)
#                     )

# # Use the metadata to create the table
# metadata.create_all(engine)

# Build a list of dictionaries: values_list
# values_list = [
#     {'state_name': '', 'fips_code': 17},
#     {'state_name': '', 'fips_code': 34},
#     {'state_name': '', 'fips_code': 38},
#     {'state_name': '', 'fips_code': 41},
#     {'state_name': '', 'fips_code': 11},
#     {'state_name': '', 'fips_code': 55},
#     {'state_name': '', 'fips_code': 4},
#     {'state_name': '', 'fips_code': 5},
#     {'state_name': '', 'fips_code': 8},
#     {'state_name': '', 'fips_code': 15},
#     {'state_name': '', 'fips_code': 20},
#     {'state_name': '', 'fips_code': 22},
#     {'state_name': '', 'fips_code': 30},
#     {'state_name': '', 'fips_code': 31},
#     {'state_name': '', 'fips_code': 40},
#     {'state_name': '', 'fips_code': 16},
#     {'state_name': '', 'fips_code': 25},
#     {'state_name': '', 'fips_code': 26},
#     {'state_name': '', 'fips_code': 29},
#     {'state_name': '', 'fips_code': 37},
#     {'state_name': '', 'fips_code': 39},
#     {'state_name': '', 'fips_code': 44},
#     {'state_name': '', 'fips_code': 45},
#     {'state_name': '', 'fips_code': 56},
#     {'state_name': '', 'fips_code': 18},
#     {'state_name': '', 'fips_code': 42},
#     {'state_name': '', 'fips_code': 46},
#     {'state_name': '', 'fips_code': 47},
#     {'state_name': '', 'fips_code': 50},
#     {'state_name': '', 'fips_code': 2},
#     {'state_name': '', 'fips_code': 10},
#     {'state_name': '', 'fips_code': 21},
#     {'state_name': '', 'fips_code': 28},
#     {'state_name': '', 'fips_code': 51},
#     {'state_name': '', 'fips_code': 12},
#     {'state_name': '', 'fips_code': 24},
#     {'state_name': '', 'fips_code': 32},
#     {'state_name': '', 'fips_code': 53},
#     {'state_name': '', 'fips_code': 6},
#     {'state_name': '', 'fips_code': 9},
#     {'state_name': '', 'fips_code': 13},
#     {'state_name': '', 'fips_code': 19},
#     {'state_name': '', 'fips_code': 23},
#     {'state_name': '', 'fips_code': 33},
#     {'state_name': '', 'fips_code': 35},
#     {'state_name': '', 'fips_code': 48},
#     {'state_name': '', 'fips_code': 1},
#     {'state_name': '', 'fips_code': 27},
#     {'state_name': '', 'fips_code': 36},
#     {'state_name': '', 'fips_code': 49},
#     {'state_name': '', 'fips_code': 54}
# ]

# # Build an insert statement for the data table: stmt
# stmt = flat_census.insert()

# # Execute stmt with the values_list: results
# results = connection.execute(stmt, values_list)

# # Print rowcount
# print(results.rowcount)

# Reflect flat_census table via engine: flat_census
flat_census = Table(
    'flat_census', metadata, autoload=True, autoload_with=engine)

# Reflect state_fact table via engine: state_fact
state_fact = Table('state_fact', metadata, autoload=True, autoload_with=engine)

# Build a statement to select name from state_fact: fips_stmt
fips_stmt = select([state_fact.columns.name])

# Append a where clause to match the fips_state
# to flat_census fips_code: fips_stmt
fips_stmt = fips_stmt.where(
    state_fact.columns.fips_state == flat_census.columns.fips_code)

# Build an update statement to set the name to fips_stmt_where: update_stmt
update_stmt = update(flat_census).values(state_name=fips_stmt)

# Execute update_stmt: results
results = connection.execute(update_stmt)

# Print rowcount
print(results.rowcount)
