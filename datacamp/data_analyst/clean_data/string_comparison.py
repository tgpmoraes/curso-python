import pandas as pd
import restaurant_data
from fuzzywuzzy import process


restaurants = pd.DataFrame(restaurant_data.rest_values)
restaurants.columns = restaurant_data.rest_columns

categories = ['italian', 'asian', 'american']

# Store the unique values of cuisine_type in unique_types
# unique_types = restaurants['cuisine_type'].unique()

# Calculate similarity of 'asian' to all values of unique_types
# print(process.extract('asian', unique_types, limit=len(unique_types)))

# Calculate similarity of 'american' to all values of unique_types
# print(process.extract('american', unique_types, limit=len(unique_types)))

# Calculate similarity of 'italian' to all values of unique_types
# print(process.extract('italian', unique_types, limit=len(unique_types)))

# Iterate through categories
for cuisine in categories:
    # Create a list of matches, comparing cuisine with the cuisine_type column
    matches = process.extract(
        cuisine,
        restaurants['cuisine_type'],
        limit=len(restaurants.cuisine_type)
    )

    # Iterate through the list of matches
    for match in matches:
        # Check whether the similarity score is greater than or equal to 80
        if match[1] >= 80:
            # If it is, select all rows where the cuisine_type is spelled
            # this way, and set them to the correct cuisine
            restaurants.loc[restaurants['cuisine_type'] == match[0]] = cuisine

# Inspect the final result
print(restaurants['cuisine_type'].unique())
