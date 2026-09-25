import mysql.connector
#  to import mysql connector

mydb = mysql.connector.connect(host="localhost", user="root", password="tiger", database= "sonal")

print("Connected successfully ✅")

mycursor = mydb.cursor()


mycursor.execute("select * from IMCC1")


# result = mycursor.fetchall()
# it will fetch all the data from the database=sonal

result = mycursor.fetchone()
# it will fetch only one data

for i in result:
    print(i)


# ---------------------------------------------------------------------
# mycursor.execute("select * from IMCC1 where age=19")


# for i in mycursor:
#     print(i)

