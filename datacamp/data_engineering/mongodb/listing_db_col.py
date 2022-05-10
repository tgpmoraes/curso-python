import pymongo


CONNECTION_STRING = "mongodb://aztgpmcan:bDCdNXag4EGBmPUHgSFcP6hF5ZN9l96YMu21V7f35YDT73hFEuu5btuC9iFayo2ITr8inAspYSKBprPhKzKwWQ==@aztgpmcan.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@aztgpmcan@"
client = pymongo.MongoClient(CONNECTION_STRING)

# Save a list of names of the databases managed by client
db_names = client.list_database_names()
print(db_names)

# Save a list of names of the collections managed by the "nobel" database
nobel_coll_names = client.nobel.list_collection_names()
print(nobel_coll_names)