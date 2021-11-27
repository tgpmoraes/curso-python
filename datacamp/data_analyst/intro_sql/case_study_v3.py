# Import create_engine, MetaData
from sqlalchemy import create_engine, MetaData, Table, select, func
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

# Select sex and average age weighted by 2000 population
stmt = select([(func.sum(census.columns.pop2000 * census.columns.age)
                / func.sum(census.columns.pop2000)).label('average_age'),
               census.columns.sex
               ])

# Group by sex
stmt = stmt.group_by(census.columns.sex)

# Execute the query and fetch all the results
results = connection.execute(stmt).fetchall()

# Print the sex and average age column for each result
for result in results:
    print(result.sex, result.average_age)
