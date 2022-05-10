import pymongo
import json
import ast
from pymongo import InsertOne
import os

curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_engineering\\mongodb\\dataset'
os.chdir(data_dir)


def read_params():
    with open('../parameters.json', 'r') as openfile:
        params = json.load(openfile)
    return params['CONNECTION_STRING']


CONNECTION_STRING = read_params()
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.nobel
collection = db.prizes
requesting = []

data = []
with open("prizes.json", "r") as inFile:
    data = ast.literal_eval(inFile.read())
for jsonObj in data[:9]:
    # print(json.loads(jsonObj))
    # myDict = json.loads(jsonObj)
    requesting.append(InsertOne(jsonObj))

result = collection.bulk_write(requesting)
client.close()
