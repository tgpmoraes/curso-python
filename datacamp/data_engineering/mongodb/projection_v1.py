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

# Use projection to select only firstname and surname
docs = db.laureates.find(
    filter={"firstname": {"$regex": "^G"},
            "surname": {"$regex": "^S"}},
    projection=["firstname", "surname"])

# Iterate over docs and concatenate first name and surname
full_names = [doc["firstname"] + " " + doc["surname"] for doc in docs]

# Print the full names
print(full_names)
