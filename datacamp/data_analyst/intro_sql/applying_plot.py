# Import create_engine function
from sqlalchemy import create_engine, Table, MetaData, select, func, desc
import pandas as pd
import matplotlib.pyplot as plt
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

# Reflect census table via engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Build an expression to calculate the sum of pop2008 labeled as population
pop2008_sum = func.sum(census.columns.pop2008).label('population')

# Build a query to select the state and sum of pop2008: stmt
stmt = select([census.columns.state, pop2008_sum])

# Group stmt by state
stmt = stmt.group_by(census.columns.state).order_by(desc(pop2008_sum))

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Create a DataFrame from the results: df
df = pd.DataFrame(results)

# Set column names
df.columns = results[0].keys()

# Print the DataFrame
print(df)

# Plot the DataFrame
df.plot.bar()
plt.xlabel('State')
plt.ylabel('Population in Millons')
plt.show()
