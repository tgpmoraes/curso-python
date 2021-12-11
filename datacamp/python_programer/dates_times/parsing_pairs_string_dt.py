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

onebike_datetime_strings = onebike_datetimes_pd.values.tolist()

# Write down the format string
fmt = "%Y-%m-%d %H:%M:%S"

# Initialize a list for holding the pairs of datetime objects
onebike_datetimes = []

# Loop over all trips
for (start, end) in onebike_datetime_strings:
    trip = {'start': datetime.strptime(start, fmt),
            'end': datetime.strptime(end, fmt)}

    # Append the trip
    onebike_datetimes.append(trip)

# Pull out the start of the first trip
first_start = onebike_datetimes[0]['start']

# Format to feed to strftime()
fmt = "%Y-%m-%dT%H:%M:%S"

# Print out date with .isoformat(), then with .strftime() to compare
print(first_start.isoformat())
print(first_start.strftime(fmt))
