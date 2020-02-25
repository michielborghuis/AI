import pymongo

client = pymongo.MongoClient('localhost', 27017)
database = client['huwebshop']
collection1 = database['products']
collection2 = database['profiles']
collection3 = database['sessions']

doc = collection1.find({})

for x in doc:
    print(x)