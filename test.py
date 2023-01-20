import pymongo
db_name = 'to_do_list'
test_client = pymongo.MongoClient('mongodb://localhost:27017')
test_db = test_client[db_name]


def check_for_db(test_client, db_name):
    dblist = test_client.list_database_names()
    if db_name in dblist:
        print(db_name + ' ← database exists')
    else:
        print(db_name + ' ← database does NOT exists')


check_for_db(test_client, db_name)  # check if database exists or not
