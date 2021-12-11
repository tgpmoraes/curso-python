# Import datetime
from datetime import datetime

# Create a datetime object
dt = datetime(year=2017, month=10, day=1, hour=15, minute=26, second=26)

# Print the results in ISO 8601 format
print(dt.isoformat())

# Create a datetime object
dt = datetime(2017, 12, 31, 15, 19, 13)

# Print the results in ISO 8601 format
print(dt.isoformat())

# Replace the year with 1917
dt_old = dt.replace(year=1917)

# Print the results in ISO 8601 format
print(dt_old)
