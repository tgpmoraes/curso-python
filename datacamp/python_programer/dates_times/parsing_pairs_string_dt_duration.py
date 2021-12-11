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

# Initialize a list for all the trip durations
onebike_durations = []

for trip in onebike_datetimes:
    # Create a timedelta object corresponding to the length of the trip
    trip_duration = trip['end'] - trip['start']

    # Get the total elapsed seconds in trip_duration
    trip_length_seconds = trip_duration.total_seconds()

    # Append the results to our list
    onebike_durations.append(trip_length_seconds)

# What was the total duration of all trips?
total_elapsed_time = sum(onebike_durations)

# What was the total number of trips?
number_of_trips = len(onebike_durations)

# Divide the total duration by the number of trips
print(total_elapsed_time / number_of_trips)

# Calculate shortest and longest trips
shortest_trip = min(onebike_durations)
longest_trip = max(onebike_durations)

# Print out the results
print("The shortest trip was " + str(shortest_trip) + " seconds")
print("The longest trip was " + str(longest_trip) + " seconds")
