# Load pandas as pd
import pandas as pd
import requests
# from pandas.io.json import json_normalize

# Load the daily report to a data frame
pop_in_shelters = pd.read_json('dhs_daily_report.json')

# View summary stats about pop_in_shelters
# print(pop_in_shelters.describe())

api_url = "https://api.yelp.com/v3/businesses/search"

# Get data about NYC cafes from the Yelp API
headers = {'Authorization': 'Bearer '}
params = {'term': 'cafe', 'location': 'NYC'}
response = requests.get(api_url,
                        headers=headers,
                        params=params)

# Extract JSON data from the response
data = response.json()
print(data)

# Load data to a data frame
# cafes = pd.DataFrame(data['businesses'])

# View the data's dtypes
# print(cafes.dtypes)

# Create dictionary that passes Authorization and key string
# headers = {'Authorization': "Bearer {}".format(api_key)}

# # Query the Yelp API with headers and params set
# response = requests.get(api_url,
#                         headers=headers,
#                         params=params)


# # Extract JSON data from response
# data = response.json()

# # Load "businesses" values to a data frame and print names
# cafes = pd.DataFrame(data['businesses'])
# print(cafes.name)

# Load other business attributes and set meta prefix
# flat_cafes = json_normalize(data["businesses"],
#                             sep="_",
#                     		record_path="categories",
#                     		meta=['name',
#                                   'alias',
#                                   'rating',
#                           		  ['coordinates', 'latitude'],
#                           		  ['coordinates', 'longitude']],
#                     		meta_prefix='biz_')
# # View the data
# print(flat_cafes.head())
# Add an offset parameter to get cafes 51-100
# params = {"term": "cafe",
#           "location": "NYC",
#           "sort_by": "rating",
#           "limit": 50,
#           "offset": 50}

# result = requests.get(api_url, headers=headers, params=params)
# next_50_cafes = json_normalize(result.json()["businesses"])

# # Append the results, setting ignore_index to renumber rows
# cafes = top_50_cafes.append(next_50_cafes, ignore_index=True)

# # Print shape of cafes
# print(cafes.shape)

# Merge crosswalk into cafes on their zip code fields
# cafes_with_pumas = cafes.merge(crosswalk,
# left_on='location_zip_code', right_on='zipcode')


# # Merge pop_data into cafes_with_pumas on puma field
# cafes_with_pop = cafes_with_pumas.merge(pop_data, on='puma')

# # View the data
# print(cafes_with_pop.head())
