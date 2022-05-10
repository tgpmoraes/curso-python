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

# original categories from 1901
original_categories = db.prizes.distinct("category", {"year": "1901"})
print(original_categories)

# project year and category, and sort
docs = db.prizes.find(
    filter={},
    projection={"year": 1, "category": 1, "_id": 0},
    sort=[("year", -1), ("category", 1)]
)

# print the documents
for doc in docs:
    print(doc)
