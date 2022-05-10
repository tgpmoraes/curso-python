import pymongo
import json
import os
from pprint import pprint


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

# Fetch prizes with quarter-share laureate(s)
filter_ = {"laureates.share": "4"}

# Save the list of field names
projection = ["category", "year", "laureates.motivation"]

# Save a cursor to yield the first five prizes
cursor = db.prizes.find(filter_, projection).sort("year").limit(5)
pprint(list(cursor))
