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

# Countries recorded as countries of death but not as countries of birth
countries = set(db.laureates.distinct("diedCountry")) - \
    set(db.laureates.distinct("bornCountry"))
print(countries)

# The number of distinct countries of laureate affiliation for prizes
count = len(set(db.laureates.distinct("prizes.affiliations.country")))
print(count)

# Save a filter for prize documents with three or more laureates
criteria = {"laureates.2": {"$exists": True}}

# Save the set of distinct prize categories in documents satisfying the
# criteria
triple_play_categories = set(db.prizes.distinct("category", criteria))

# Confirm literature as the only category not satisfying the criteria.
assert set(db.prizes.distinct("category")) - triple_play_categories == \
    {'peace', 'economics', 'literature', 'medicine'}
