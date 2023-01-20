from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

# Create a MongoClient
client = MongoClient('localhost', 27017)
db = client['todo_db']

# # # Get database instance
# coll = db['todo_db']
# print("Database created........")

# # Verification -- this command will list all current db's
# print('List of databases after creating new one')
# print(client.list_database_names())


# # Get a second test database instance
db = client['test_db']

# adding a doc to a test collection

coll = db['test_collection']

test_doc = {"text": "Test body text", "created_at": datetime.now()}
# coll.insert_one(test_doc)


# updating a doc in test collection
update_content = {"text": "This text has been updated",
                  "updated_at": datetime.now()}
updated_doc_id = {"_id": ObjectId("63cb084635a158c67e0c42bd")}
new_values = {"text": "This text has been updated",
              "updated_at": datetime.now()}

coll.update_one(updated_doc_id, {"$set": new_values})


print(coll.find_one({"_id": ObjectId("63cb084635a158c67e0c42bd")}))
# for doc in coll.find():
#     print(doc)
