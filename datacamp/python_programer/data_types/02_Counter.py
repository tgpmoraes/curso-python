import os
import csv
from collections import Counter
from datetime import datetime


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\python_programer\\data_types'
os.chdir(data_dir)

# Create the file object: csvfile
csvfile = open('crime_sampler.csv', 'r')

# Create an empty list: crime_data
crime_data = []

# Loop over a csv reader on the file object
for row in csv.reader(csvfile):

    # Append the date, type of crime, location description, and arrest
    crime_data.append((row[0], row[2], row[4], row[5]))

# Remove the first element from crime_data
crime_data.pop(0)

# Create a Counter Object: crimes_by_month
crimes_by_month = Counter()

# Loop over the crime_data list
for row in crime_data:

    # Convert the first element of each item into a
    # Python Datetime Object: date
    date = datetime.strptime(row[0], '%m/%d/%Y %I:%M:%S %p')

    # Increment the counter for the month of the row by one
    crimes_by_month[date.month] += 1

# Print the 3 most common months for crime
print(crimes_by_month.most_common(3))
