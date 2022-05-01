import pymongo
from pymongo import MongoClient
# from pymongo import collection

cluster =MongoClient('mongodb+srv://elakia:Kvtohindu@cluster0.dyhgo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = cluster['animals']
collection = db['name']

collection.insert_one({'cat':1,'dog':5})