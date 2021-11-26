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

# Print the table details
# print(repr(metadata.tables['data']))

# Build an insert statement to insert a record into the data table: insert_stmt
insert_stmt = insert(data).values(
    name='Anna', count=1, amount=1000.00, valid=True)

# Execute the insert statement via the connection: results
results = connection.execute(insert_stmt)

# Print result rowcount
print(results.rowcount)

# Build a select statement to validate the insert: select_stmt
select_stmt = select([data]).where(data.columns.name == 'Anna')

# Print the result of executing the query.
print(connection.execute(select_stmt).first())
