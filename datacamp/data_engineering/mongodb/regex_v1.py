import pymongo
import json
import os
from bson.regex import Regex

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

# Filter for laureates with "Germany" in their "bornCountry" value
criteria = {"bornCountry": Regex("Germany")}
print(set(db.laureates.distinct("bornCountry", criteria)))

# Filter for laureates with a "bornCountry" value starting with "Germany"
criteria = {"bornCountry": Regex("^Germany")}
print(set(db.laureates.distinct("bornCountry", criteria)))

# Fill in a string value to be sandwiched between the strings "^Germany "
# and "now"
criteria = {"bornCountry": Regex("^Germany " + "\(" + "now")}
print(set(db.laureates.distinct("bornCountry", criteria)))

# Filter for currently-Germany countries of birth. Fill in a string value to be 
# ndwiched between the strings "now" and "$"
criteria = {"bornCountry": Regex("now" + " Germany\)" + "$")}
print(set(db.laureates.distinct("bornCountry", criteria)))
