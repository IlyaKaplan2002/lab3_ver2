import mysql.connector

db_connection = mysql.connector.connect(
host="localhost",
user="root",
password="admin",
database="Timetable",
auth_plugin="mysql_native_password"
)

print(db_connection)

db_cursor = db_connection.cursor()

db_cursor.execute("SHOW TABLES")

ii = []

for i in db_cursor:
    print(i[0].decode('UTF-8'))
    ii.append(i[0].decode('UTF-8'))
    print(ii)
