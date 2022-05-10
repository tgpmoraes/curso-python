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

# Count prizes awarded (at least partly) to organizations as a sum
# over sizes of "prizes" arrays.
pipeline = [
    {"$match": {"gender": "org"}},
    {"$project": {"n_prizes": {"$size": ["$prizes"]}}},
    {"$group": {"_id": None, "n_prizes_total": {"$sum": "n_prizes"}}}
]

print(list(db.laureates.aggregate(pipeline)))
