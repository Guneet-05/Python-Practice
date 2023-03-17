import mysql.connector
# we have installed mysql-connector-python instead of mysql-connector
mydb = mysql.connector.connect(host="localhost",user="root", passwd="9863472",database="guneet")

mycursor = mydb.cursor()
mycursor.execute("select * from student")

for i in mycursor:
    print(i)

