import os
import json
import requests


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\inter_import\\data'
os.chdir(data_dir)

with open('parametros.json') as json_file:
    json_data = json.load(json_file)

# Assign URL to variable: url
url = f"""http://www.omdbapi.com/?apikey={json_data['apikey']}\
&t=the+social+network"""

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Print the text of the response
print(r.text)
