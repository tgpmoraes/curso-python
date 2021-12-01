from pytz import timezone
from datetime import datetime


daily_summaries = [(datetime(2001, 1, 1, 23, 19), '126455'),
                   (datetime(2001, 1, 2, 18, 58), '501952'),
                   (datetime(2001, 1, 3, 14, 34), '536432'),
                   (datetime(2001, 1, 4, 3, 56), '550011'),
                   (datetime(2001, 1, 5, 2, 50), '557917'),
                   (datetime(2001, 1, 6, 18, 18), '255356'),
                   (datetime(2001, 1, 7, 1, 27), '169825'),
                   (datetime(2001, 1, 8, 11, 3), '590706'),
                   (datetime(2001, 1, 9, 23, 35), '599905')]

# Create a Timezone object for Chicago
chicago_usa_tz = timezone('US/Central')

# Create a Timezone object for New York
ny_usa_tz = timezone('US/Eastern')

# Iterate over the daily_summaries list
for orig_dt, ridership in daily_summaries:

    # Make the orig_dt timezone "aware" for Chicago
    chicago_dt = orig_dt.replace(tzinfo=chicago_usa_tz)

    # Convert chicago_dt to the New York Timezone
    ny_dt = chicago_dt.astimezone(ny_usa_tz)

    # Print the chicago_dt, ny_dt, and ridership
    print('Chicago: %s, NY: %s, Ridership: %s' % (chicago_dt, ny_dt, ridership))
