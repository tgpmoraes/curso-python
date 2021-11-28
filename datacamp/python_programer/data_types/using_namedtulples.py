import os
import pandas as pd
from collections import namedtuple


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\python_programer\\data_types'
os.chdir(data_dir)

records = pd.read_csv('cta_daily_station_totals.csv')

entries = records[['date', 'stationname', 'rides']].values.tolist()

# Create the namedtuple: DateDetails
DateDetails = namedtuple('DateDetails', ['date', 'stop', 'riders'])

# Create the empty list: labeled_entries
labeled_entries = []

# Iterate over the entries list
for date, stop, riders in entries:
    # Append a new DateDetails namedtuple instance for each
    # entry to labeled_entries
    labeled_entries.append(DateDetails(date, stop, riders))

# Print the first 5 items in labeled_entries
print(labeled_entries[:5])

# Iterate over the first twenty items in labeled_entries
for item in labeled_entries[:20]:
    # Print each item's stop
    print(item.stop)

    # Print each item's date
    print(item.date)

    # Print each item's riders
    print(item.riders)
