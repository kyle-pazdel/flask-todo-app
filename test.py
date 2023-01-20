from pymongo import MongoClient
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
coll.insert_one(test_doc)
print(coll.find_one())
