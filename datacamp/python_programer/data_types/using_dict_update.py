import names

# Assign the names_2011 dictionary as the value to the 2011 key of boy_names
names.boy_names[2011] = names.names_2011

# Update the 2012 key in the boy_names dictionary
names.boy_names[2012].update([(1, 'Casey'), (2, 'Aiden')])

# Loop over the years in the boy_names dictionary
for year in names.boy_names:
    # Sort the data for each year by descending rank and get the lowest one
    lowest_ranked = sorted(names.boy_names[year], reverse=True)[0]
    # Safely print the year and the least popular name or 'Not Available'
    print(year, names.boy_names[year].get(lowest_ranked, 'Not Available'))
