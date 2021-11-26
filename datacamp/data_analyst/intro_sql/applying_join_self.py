# Import create_engine function
from sqlalchemy import create_engine, Table, MetaData, select
import os


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\intro_sql'
os.chdir(data_dir)

# Create an engine that connects to the employees.sqlite file: engine
engine = create_engine('sqlite:///employees.sqlite')

# Create a connection on engine
connection = engine.connect()

# Create a metadata object: metadata
metadata = MetaData()

# Reflect employees table via engine: employees
employees = Table('employees', metadata, autoload=True, autoload_with=engine)

# Make an alias of the employees table: managers
managers = employees.alias()

# Build a query to select names of managers and their employees: stmt
stmt = select(
    [managers.columns.name.label('manager'),
     employees.columns.name.label('employee')]
)

# Match managers id with employees mgr: stmt_matched
stmt_matched = stmt.where(managers.columns.id == employees.columns.mgr)

# Order the statement by the managers name: stmt_ordered
stmt_ordered = stmt_matched.order_by(managers.columns.name)

# Execute statement: results
results = connection.execute(stmt_ordered).fetchall()

# Print records
for record in results:
    print(record)
