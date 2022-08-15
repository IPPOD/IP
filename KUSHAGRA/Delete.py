import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "ip"
)

mycursor = mydb.cursor()

sql = "DELETE FROM EMPL WHERE EMPNO = '8844'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")