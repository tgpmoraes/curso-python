import os
import pandas as pd
import tires
import datetime as dt


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\clean_data\\data'
os.chdir(data_dir)

ride_sharing = pd.read_csv('ride_sharing_new.csv')
ride_sharing['tire_sizes'] = tires.tire_size

# Convert tire_sizes to integer
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('int')

# Set all values above 27 to 27
ride_sharing.loc[ride_sharing['tire_sizes'] > 27, 'tire_sizes'] = 27

# Reconvert tire_sizes back to categorical
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('category')

# Print tire size description
print(ride_sharing['tire_sizes'].describe())

# Save today's date
today = dt.datetime.today()

# Convert ride_date to datetime
ride_sharing['ride_date'] = ride_sharing['tire_sizes'].apply(
    lambda i: today.replace(year=today.year + 1))
ride_sharing['ride_dt'] = pd.to_datetime(ride_sharing['ride_date'])

# Set all in the future to today's date
ride_sharing.loc[ride_sharing['ride_dt'] > today, 'ride_dt'] = today

# Print maximum of ride_dt column
print(ride_sharing['ride_dt'].max())
