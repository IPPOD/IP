import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "ip"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")