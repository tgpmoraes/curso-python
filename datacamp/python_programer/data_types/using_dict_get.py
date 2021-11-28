import names

# Safely print rank 7 from the names dictionary
print(names.female_baby_names_2012.get(7))

# Safely print the type of rank 100 from the names dictionary
print(type(names.female_baby_names_2012.get(100)))

# Safely print rank 105 from the names dictionary or 'Not Found'
print(names.female_baby_names_2012.get(105, 'Not Found'))
