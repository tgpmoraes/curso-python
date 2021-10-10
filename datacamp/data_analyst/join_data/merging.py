import riders
import pandas as pd

cal = pd.DataFrame(
    riders.cal,
    columns=['year', 'month', 'day', 'day_type'])
ridership = pd.DataFrame(
    riders.ridership,
    columns=['station_id', 'year', 'month', 'day', 'rides'])
stations = pd.DataFrame(
    riders.stations,
    columns=['station_id', 'station_name', 'location'])

# Merge the ridership, cal, and stations tables
ridership_cal_stations = ridership.merge(cal, on=['year', 'month', 'day']) \
                                  .merge(stations, on='station_id')

# Create a filter to filter ridership_cal_stations
filter_criteria = ((ridership_cal_stations['month'] == 7)
                   & (ridership_cal_stations['day_type'] == 'Weekday')
                   & (ridership_cal_stations['station_name'] == 'Wilson'))

# Use .loc and the filter to select for rides
print(ridership_cal_stations.loc[filter_criteria, 'rides'].sum())

# Print the results by alderman and show median income
print(ridership_cal_stations.groupby(['station_id', 'year'])
                            .agg({'rides': 'sum'}))
