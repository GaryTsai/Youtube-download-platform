import pymongo

# client=pymongo.MongoClient(['localhost:27017'])
# DATABASE = client['test1']

class Database(object):
     URL = ['localhost:27017']
     DATABASE = None

     @staticmethod
     def initialize():
         client = pymongo.MongoClient(Database.URL)
         Database.DATABASE = client['project']

     @staticmethod
     def insert(collection,data):
         Database.DATABASE[collection].insert(data)

     @staticmethod
     def find(collection,query):
         return Database.DATABASE[collection].find(query)
     @staticmethod
     def find_one(collection , query):
         return Database.DATABASE[collection].find_one(query)

     @staticmethod
     def remove(collection,query):
         Database.DATABASE[collection].remove(query)
