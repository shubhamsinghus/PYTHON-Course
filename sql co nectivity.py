import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root@123",
  database="sql_hazard",
  auth_plugin='mysql_native_password'
)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
#mydb.commit()
data = mycursor.fetchall()
for x in data:
    print(x)
