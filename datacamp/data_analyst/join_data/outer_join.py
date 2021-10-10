# import matplotlib.pyplot as plt
import pandas as pd
import os


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\join_data'
os.chdir(data_dir)

movies = pd.read_pickle('movies.p')
casts = pd.read_pickle('casts.p').drop(
    labels=['cast_id', 'gender'],
    axis='columns'
)

iron_1_actors = casts[casts['movie_id'] == 1726].drop(
    labels='movie_id',
    axis='columns')
iron_2_actors = casts[casts['movie_id'] == 10138].drop(
    labels='movie_id',
    axis='columns')

# Merge iron_1_actors to iron_2_actors on id with outer join using suffixes
iron_1_and_2 = iron_1_actors.merge(iron_2_actors,
                                   on='id',
                                   how='outer',
                                   suffixes=('_1', '_2'))

# Create an index that returns true if name_1 or name_2 are null
m = ((iron_1_and_2['name_1'].isnull()) |
     (iron_1_and_2['name_2'].isnull()))

# Print the first few rows of iron_1_and_2
print(iron_1_and_2[m].head())
