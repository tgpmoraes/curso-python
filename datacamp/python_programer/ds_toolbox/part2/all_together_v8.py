# Import pandas
import os
import pandas as pd


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\python_programer\\ds_toolbox'
os.chdir(data_dir)


# Initialize reader object: df_reader
df_reader = pd.read_csv('world_ind_pop_data.csv', chunksize=10)

# Print two chunks
print(df_reader.get_chunk())
print(df_reader.get_chunk())
