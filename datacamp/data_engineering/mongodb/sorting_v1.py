import pymongo
import json
import os
from operator import itemgetter


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_engineering\\mongodb'
os.chdir(data_dir)


def read_params():
    with open('parameters.json', 'r') as openfile:
        params = json.load(openfile)
    return params['CONNECTION_STRING']


def all_laureates(prize):
    # sort the laureates by surname
    sorted_laureates = sorted(prize["laureates"], key=itemgetter("surname"))

    # extract surnames
    surnames = [laureate["surname"] for laureate in sorted_laureates]

    # concatenate surnames separated with " and "
    all_names = " and ".join(surnames)

    return all_names


CONNECTION_STRING = read_params()
client = pymongo.MongoClient(CONNECTION_STRING)

# Connect to the "nobel" database
db = client.nobel

# find physics prizes, project year and name, and sort by year
docs = db.prizes.find(
    filter={"category": "physics"},
    projection=["year", "laureates.firstname", "laureates.surname"],
    sort=[("year", 1)])

# print the year and laureate names (from all_laureates)
for doc in docs:
    print("{year}: {names}".format(year=doc["year"], names=all_laureates(doc)))
