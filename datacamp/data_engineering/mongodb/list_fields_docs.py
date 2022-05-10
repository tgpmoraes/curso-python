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

# Retrieve sample prize and laureate documents
prize = db.prizes.find_one()
laureate = db.laureates.find_one()

# Print the sample prize and laureate documents
print(prize)
print(laureate)
print(type(laureate))

# Get the fields present in each type of document
prize_fields = list(prize.keys())
laureate_fields = list(laureate.keys())

print(prize_fields)
print(laureate_fields)
