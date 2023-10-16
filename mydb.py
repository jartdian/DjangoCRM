import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root'

)

cursorObject = dataBase.cursor()

#create a db
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")