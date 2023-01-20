import pymongo
from datetime import datetime

# name database and set mongo client
# db_name = 'to_do_list'
# test_client = pymongo.MongoClient('mongodb://localhost:27017')
# test_db = test_client[db_name]


# def check_for_db(test_client, db_name):
#     dblist = test_client.list_database_names()
#     if db_name in dblist:
#         print(db_name + ' ← database exists')
#     else:
#         print(db_name + ' ← database does NOT exists')


# check_for_db(test_client, db_name)  # check if database exists or not

# make collection in db
# col_name = 'tasks'
# test_col = test_db[col_name]


# def check_for_col(test_db, col_name):
#     collist = test_db.list_collection_names()
#     if col_name in collist:
#         print(col_name + ' <-- collection exists')
#     else:
#         print(col_name + ' <-- collection does NOT exists')


# check_for_col(test_db, col_name)

# create a dictionary to be added to the first collection
# now = datetime.now()
# test_dict = {"title": "Work on practice project",
#              "completed": False, "created_at": now}
# pl = test_col.insert_one(test_dict)

# print(pl.inserted_id)


# insert many tasks to the collection

db_name = 'to_do_list'
col_name = 'tasks'
test_client = pymongo.MongoClient("mongodb://localhost:27017/")
test_db = test_client[db_name]
test_col = test_db[col_name]


now = datetime.now()

test_list = [{"title": "Go to grocery store", "completed": False, "created_at": now},
             {"title": "Work out", "completed": False, "created_at": now},
             {"title": "Solve algorithm problem",
                 "completed": False, "created_at": now},
             {"title": "Make dinner", "completed": False, "created_at": now}]

pl = test_client['to_do_list']['tasks'].insert_many(test_list)

# print list of id's for values of inserted players
print(pl.inserted_ids)

#  print list of dicts in db
# list(test_db.collection.find({}))
