import pymongo
import json
import os
from collections import OrderedDict


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

original_categories = sorted(
    set(db.prizes.distinct("category", {"year": "1901"})))
pipeline = [
    {"$match": {"category": {"$in": original_categories}}},
    {"$project": {"category": 1, "year": 1}},

    # Collect the set of category values for each prize year.
    {"$group": {"_id": "$year", "categories": {"$addToSet": "$category"}}},

    # Project categories *not* awarded (i.e., that are missing this year).
    {"$project": {"missing": {"$setDifference": [
        original_categories, "$categories"]}}},

    # Only include years with at least one missing category
    {"$match": {"missing.0": {"$exists": True}}},

    # Sort in reverse chronological order. Note that "_id" is a distinct year
    # at this stage.
    {"$sort": OrderedDict([("_id", -1)])},
]
for doc in db.prizes.aggregate(pipeline):
    print("{year}: {missing}".format(
        year=doc["_id"], missing=", ".join(sorted(doc["missing"]))))
