import pymongo
import json
import os

curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_engineering\\mongodb'
os.chdir(data_dir)


def read_params():
    with open('parameters.json', 'r') as openfile:
        params = json.load(openfile)
    return params['CONNECTION_STRING']


CONNECTION_STRING = read_params()
client = pymongo.MongoClient(CONNECTION_STRING)

# Connect to the "nobel" database
db = client.nobel

# Create a filter for Germany-born laureates who died in the USA and with the
# first name "Albert"
criteria = {"diedCountry": "USA",
            "bornCountry": "Germany",
            "firstname": "Albert"}

# Save the count
count = db.laureates.count_documents(criteria)
print(count)

# Save a filter for laureates born in the USA, Canada, or Mexico
criteria = {"bornCountry":
            {"$in": ["USA", "Canada", "Mexico"]}
            }

# Count them and save the count
count = db.laureates.count_documents(criteria)
print(count)

# Save a filter for laureates who died in the USA and were not born there
criteria = {"diedCountry": "USA",
            "bornCountry": {"$ne": "USA"},
            }

# Count them
count = db.laureates.count_documents(criteria)
print(count)
