

import pymongo

client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

mydb = client['akshay']
info = mydb.collections.info
# print(info.find())
# info.insert_one({'name': 'arpit', 'Gf': 'Radhika'})

# Select * from info;
# for record in info.find({}):
#     print(record)

# info.insert_many([{'name': 'valishali', 'age': '20'}, {'name': 'aayush', 'age': '16'}, {
#                  'name': "Papa", 'age': '54', 'birthday': '4th April'}])

# for record in info.find({'name': 'Papa', 'age': '54'}):
#     print(record)

# print(info.find_one())

# Select * from info where name in ();
# for record in info.find({'name': {'$in': ['arpit', 'akshay']}}):
#     print(record)

# select * from info where age>35;
# for record in info.find({'age': {'$gt': '35'}}):
#     print(record)


# # select * from info where name='akshay' or Gf='Radhika';
# for record in info.find({'$or': [{'name': 'akshay'}, {'Gf': 'Radhika'}]}):
#     print(record)
# # select * from info where name='akshay' and Gf='Radhika';
# for record in info.find({'$and': [{'name': 'akshay'}, {'Gf': 'Radhika'}]}):
#     print(record)


# Updating Records
# info.update_one(
#     {'name': 'Papa'},
#     {'$set': {'age': '24'},
#      "$currentDate": {'Modified_Date': True}})
# for record in info.find({'name': 'Papa'}):
# print(record)

# Update_Multiple_Records
# info.update_many(
#     {'name': 'Papa'},
#     {'$set': {'age': '64'},
#      "$currentDate": {'Modified_Date': True}})

# for record in info.find({'name': 'Papa'}):
#     print(record)

# info.update_many(
#     {"age": '14'},
#     {"$set": {"age": 14}}
# )

# Replace to whole Json here
# info.replace_one(
#     {'name':'Papa'},
#     {'name':'PapaJi','age':'44','Occupation':'LIC'}
# )

# Agreegate Functions


# for record in info.find({}):
#     print(record)


# data = info.aggregate([
#     {"$group": {
#         "_id": "$name",
#         "No Of Records": {"$sum": 1}
#     }}
# ])

# for row in data:
#     print(row)

# for record in info.find({}):
#     print(record)

data = info.aggregate([
    {"$group": {
        "_id": "$name",
        "Avg Age": {"$avg": "$age"},
        "No of Records": {"$sum": 1}
    }}
])


for row in data:
    print(row)


# Project

# select name,age from info; // Selecting few columns from table
data = info.aggregate([
    {"$project": {'name': 1, 'Gf': 1}}
])

for row in data:
    print(row)
