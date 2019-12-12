import pymongo

client = pymongo.MongoClient("localhost", 27017)

db = client.test

stu = db.stu

for cur in stu.find():
    print(cur)
