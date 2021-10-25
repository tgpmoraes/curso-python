# Import necessary module
import os
from sqlalchemy import create_engine
import pandas as pd


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\intro_import\\data'
os.chdir(data_dir)

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

query = '''
select Title, Name
from Album
inner join Artist
on Album.ArtistID = Artist.ArtistID'''

# Execute query and store records in DataFrame: df
df = pd.read_sql_query(query, engine)

# Print head of DataFrame
print(df.head())
