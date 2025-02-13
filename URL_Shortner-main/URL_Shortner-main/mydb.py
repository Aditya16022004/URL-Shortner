import mysql.connector

dataBase = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Kamal1395",
)


cursorObject = dataBase.cursor()


cursorObject.execute("CREATE DATABASE basedir")

print("Database created")