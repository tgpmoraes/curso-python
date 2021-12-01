import crimes_list
# Import the datetime object from datetime
from datetime import datetime


datetimes_list = []

# Iterate over the dates_list
for date_str in crimes_list.dates_list:
    # Convert each date to a datetime object: date_dt
    date_dt = datetime.strptime(date_str, '%m/%d/%Y')

    datetimes_list.append(date_dt)

# Loop over the first 10 items of the datetimes_list
for item in datetimes_list[:10]:
    # Print out the record as a string in the format of 'MM/DD/YYYY'
    print(datetime.strftime(item, '%m/%d/%Y'))

    # Print out the record as an ISO standard string
    print(datetime.isoformat(item))
