import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "ip"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM EMPL WHERE EMPNO='8369'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for q in myresult:
  print(q)