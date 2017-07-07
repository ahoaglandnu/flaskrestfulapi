import pymongo
client = pymongo.MongoClient()

# create the db
db = client.restdb

# create the collection
collection = db['star']

# data for collection
docs = [{"name": "Betelgeuse","distance":643},{"name":"Sirius","distance":8.6},{"name":"Bellatrix","distance":243}]

# insert data into collection
docs_id = collection.insert_many(docs)

# verify
import pprint
for docs in collection.find():
	pprint.pprint(docs)