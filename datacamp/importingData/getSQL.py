# Import sqlalchemy's create_engine() function
from sqlalchemy import create_engine
import pandas as pd

# Create the database engine
file_path = 'Streamlined-Data-Ingestion-with-pandas-Datacamp-main'
engine = create_engine(f'sqlite:///../{file_path}/data.db')

# View the tables in the database
# print(engine.table_names())

# Load hpd311calls without any SQL
hpd_calls = pd.read_sql_table('hpd311calls', engine)

# View the first few rows of data
# print(hpd_calls.head())

# Create a SQL query to load the entire weather table
query = """
SELECT *
FROM weather;
"""

# Load weather with the SQL query
weather = pd.read_sql(query, engine)

# View the first few rows of data
print(weather.head())
