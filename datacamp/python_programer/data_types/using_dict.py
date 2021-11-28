import names

# Create an empty dictionary: names_by_rank
names_by_rank = {}

# Loop over the girl names
for rank, name in names.female_baby_names_2012.items():
    # Add each name to the names_by_rank dictionary using rank as the key
    names_by_rank[rank] = name

# Sort the names_by_rank dict by rank in descending order
# and slice the first 10 items
for rank in sorted(names_by_rank, reverse=True)[:10]:
    # Print each item
    print(names_by_rank[rank])

# Safely print rank 7 from the names dictionary
print(names.female_baby_names_2012.get(7))

# Safely print the type of rank 100 from the names dictionary
print(type(names.female_baby_names_2012.get(100)))

# Safely print rank 105 from the names dictionary or 'Not Found'
print(names.female_baby_names_2012.get(105, 'Not Found'))
