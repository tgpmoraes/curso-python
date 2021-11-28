import os
import pandas as pd
from collections import defaultdict


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\python_programer\\data_types'
os.chdir(data_dir)

records = pd.read_csv('cta_daily_station_totals.csv')

entries = records[['date', 'stationname', 'rides']].values.tolist()

# Create a defaultdict with a default type of list: ridership
ridership = defaultdict(list)

# Iterate over the entries
for date, stop, riders in entries:
    # Use the stop as the key of ridership and append the riders to its value
    ridership[stop].append(riders)

# Print the first 10 items of the ridership dictionary
print(list(ridership.items())[:10])
