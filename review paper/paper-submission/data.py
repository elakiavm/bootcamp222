    import pymongo

    cluster=pymongo.MongoClient("mongodb://localhost:27017/")
    db = cluster["Paper_review"]
    col = db["Name"]


    for x in collection.find():
        print(x) 