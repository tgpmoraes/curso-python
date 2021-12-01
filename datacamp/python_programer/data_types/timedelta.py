import os
import pandas as pd
from datetime import timedelta, datetime


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\python_programer\\data_types'
os.chdir(data_dir)

records = pd.read_csv('cta_daily_summary_totals.csv')
records = records[['service_date', 'total_rides', 'day_type']]
records['service_date'] = records['service_date'].astype(
    'datetime64[ns]')

daily_summaries = {}

for row in records.iterrows():
    daily_summaries[row[1][0]] = {
        'day_type': row[1][2],
        'total_ridership': row[1][1]}

# Build a timedelta of 30 days: glanceback
glanceback = timedelta(days=30)

review_dates = [datetime(2013, 12, 22, 0, 0),
                datetime(2013, 12, 23, 0, 0),
                datetime(2013, 12, 24, 0, 0),
                datetime(2013, 12, 25, 0, 0),
                datetime(2013, 12, 26, 0, 0),
                datetime(2013, 12, 27, 0, 0),
                datetime(2013, 12, 28, 0, 0),
                datetime(2013, 12, 29, 0, 0),
                datetime(2013, 12, 30, 0, 0),
                datetime(2013, 12, 31, 0, 0)]

# Iterate over the review_dates as date
for date in review_dates:
    # Calculate the date 30 days back: prior_period_dt
    prior_period_dt = date - glanceback

    # Print the review_date, day_type and total_ridership
    print('Date: %s, Type: %s, Total Ridership: %s' %
          (date,
           daily_summaries[date]['day_type'],
           daily_summaries[date]['total_ridership']))

    # Print the prior_period_dt, day_type and total_ridership
    print('Date: %s, Type: %s, Total Ridership: %s' %
          (prior_period_dt,
           daily_summaries[prior_period_dt]['day_type'],
           daily_summaries[prior_period_dt]['total_ridership']))
