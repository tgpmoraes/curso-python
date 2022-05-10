# Import package
import requests

# Assign URL to variable: url
url = '''https://masterdataapi.nobelprize.org/2.1/nobelPrizes?\
offset=0&limit=25'''

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print the Wikipedia page extract
pizza_extract = json_data['nobelPrizes'][0]['laureates']
print(pizza_extract)
