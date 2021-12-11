import os
import pandas as pd
from datetime import datetime


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\python_programer\\dates_times'
os.chdir(data_dir)

records = pd.read_csv('capital-onebike.csv')

onebike = records[records['Bike number'] == 'W20529']
onebike_datetimes_pd = onebike[['Start date', 'End date']]
onebike_datetimes_pd.columns = ['start_date', 'end_date']

onebike_datetimes = []

format = "%Y-%m-%d %H:%M:%S"

onebike_datetimes.append(onebike_datetimes_pd.apply(
    lambda row: {'end': datetime.strptime(row.end_date, format),
                 'start': datetime.strptime(row.start_date, format)},
    axis=1
).values.tolist())

onebike_datetimes = onebike_datetimes[0]

# Create dictionary to hold results
trip_counts = {'AM': 0, 'PM': 0}

# Loop over all trips
for trip in onebike_datetimes:
    # Check to see if the trip starts before noon
    if trip['start'].hour < 12:
        # Increment the counter for before noon
        trip_counts['AM'] += 1
    else:
        # Increment the counter for after noon
        trip_counts['PM'] += 1

print(trip_counts)
