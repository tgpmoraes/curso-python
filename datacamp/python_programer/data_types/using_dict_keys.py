import names

# Print a list of keys from the boy_names dictionary
print(names.boy_names.keys())

# Print a list of keys from the boy_names dictionary for the year 2013
print(names.boy_names[2013].keys())

# Loop over the dictionary
for year in names.boy_names:
    # Safely print the year and the third ranked name or 'Unknown'
    print(year, names.boy_names[year].get(3, 'Unknown'))
