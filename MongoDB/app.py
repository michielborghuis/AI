import pymongo

client = pymongo.MongoClient('localhost', 27017)
database = client['huwebshop']
collection1 = database['products']
collection2 = database['profiles']
collection3 = database['sessions']

results = collection1.find({})

for result in results[:1]:
    print(result["name"])
    print(result["price"])