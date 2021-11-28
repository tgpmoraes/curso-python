import os
import pandas as pd
from collections import Counter


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\python_programer\\data_types'
os.chdir(data_dir)

records = pd.read_csv('cta_daily_station_totals.csv')

stations = records['stationname'].values.tolist()

# Print the first ten items from the stations list
print(stations[:10])

# Create a Counter of the stations list: station_count
station_count = Counter(stations)

# Print the station_count
print(station_count)

# Find the 5 most common elements
print(station_count.most_common(5))
