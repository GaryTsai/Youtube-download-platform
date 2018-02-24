from common.database import Database

Database.initialize()
Database.insert('users',{"account":"kest8088","password":"123456","name":"gary"})
user = Database.find_one('users',{"account":"kest8088"})
print(user)