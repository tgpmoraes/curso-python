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


# Filter for laureates born in Austria with non-Austria prize affiliation
criteria = {"bornCountry": "USA",
            "prizes.affiliations.country": {"$ne": "Austria"}}

# Count the number of such laureates
count = db.laureates.count_documents(criteria)
print(count)

# Filter for documents without a "born" field
criteria = {"born": {"$exists": False}}

# Save count
count = db.laureates.count_documents(criteria)
print(count)

# Filter for laureates with at least three prizes
criteria = {"prizes.0": {"$exists": True}}

# Find one laureate with at least three prizes
doc = db.laureates.find_one(criteria)

# Print the document
print(doc)
