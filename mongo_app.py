import pymongo 
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://elakia:Kvtohindu@cluster0.dyhgo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = cluster["demo1"] 
collection = db["flower"]

# collection.insert_one({'_id':2,'sunflower':20,'lily':25})
myquery = {'_id':1}
# mydoc = collection.find(myquery)
# print(mydoc)
# for x in mydoc:
#   print(x)
# collection.delete_one(myquery)
myquery = { "sunflower": 20}
newvalues = { "$set": { "address": "Canyon 123" } }
collection.update_one(myquery, newvalues)