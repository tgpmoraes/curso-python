# Import Table, Column, String, Integer, Float, Boolean from sqlalchemy
from sqlalchemy import create_engine, Table, MetaData, select,\
    Table, Column, String, Integer, Float, Boolean, insert


# Create an engine that connects to the census.sqlite file: engine
engine = create_engine('sqlite:///:memory:')

# Create a connection on engine
connection = engine.connect()

# Create a metadata object: metadata
metadata = MetaData()

# Define a new table with a name, count, amount, and valid column: data
data = Table('data', metadata,
             Column('name', String(255), unique=True),
             Column('count', Integer(), default=1),
             Column('amount', Float()),
             Column('valid', Boolean(), default=False)
             )

# Use the metadata to create the table
metadata.create_all(engine)

# Build a list of dictionaries: values_list
values_list = [
    {'name': 'Anna', 'count': 1, 'amount': 1000.00, 'valid': True},
    {'name': 'Taylor', 'count': 1, 'amount': 750.00, 'valid': False}
]

# Build an insert statement for the data table: stmt
stmt = data.insert()

# Execute stmt with the values_list: results
results = connection.execute(stmt, values_list)

# Print rowcount
print(results.rowcount)
