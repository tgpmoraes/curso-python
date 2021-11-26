# Import create_engine function
from sqlalchemy import create_engine, Table, MetaData, select, func
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

# Build a query to select names of managers and counts of their employees: stmt
stmt = select([managers.columns.name, func.count(employees.columns.id)])

# Append a where clause that ensures the manager id and employee mgr are equal
stmt_matched = stmt.where(managers.columns.id == employees.columns.mgr)

# Group by Managers Name
stmt_grouped = stmt_matched.group_by(managers.columns.name)

# Execute statement: results
results = connection.execute(stmt_grouped).fetchall()

# print manager
for record in results:
    print(record)
