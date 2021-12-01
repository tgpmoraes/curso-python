import os
import csv
from collections import defaultdict


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\python_programer\\data_types'
os.chdir(data_dir)

# Create the file object: csvfile
csvfile = open('crime_sampler.csv', 'r')

# Create a dictionary that defaults to a list: crimes_by_block
crimes_by_block = defaultdict(list)

# Loop over a DictReader of the CSV file
for row in csv.DictReader(csvfile):
    # Pop the block from each row: block
    block = row.pop('Block')
    # Append the rest of the data to the list for proper block
    # in crimes_by_block
    crimes_by_block[block].append(row['Primary Type'])

# Create a unique list of crimes for the first block: n_state_st_crimes
n_state_st_crimes = set(crimes_by_block['001XX N STATE ST'])

# Print the list
print(n_state_st_crimes)

# Create a unique list of crimes for the second block: w_terminal_st_crimes
w_terminal_st_crimes = set(crimes_by_block['0000X W TERMINAL ST'])

# Print the list
print(w_terminal_st_crimes)

# Find the differences between the two blocks: crime_differences
crime_differences = n_state_st_crimes.difference(w_terminal_st_crimes)

# Print the differences
print(crime_differences)
