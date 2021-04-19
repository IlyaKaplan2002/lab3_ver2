import mysql.connector
from method1 import *
from method2 import *
from method3 import *
from method4 import *
from method5 import *

db_connection = mysql.connector.connect(
host="localhost",
user="root",
password="admin",
database="Timetable",
auth_plugin="mysql_native_password"
)

db_cursor = db_connection.cursor()

run = True

while run:

    print("This is a python programm which is used to manage a Timetable database.")
    print("Methods:")
    print("1-create a new note;")
    print("2-edit a note;")
    print("3-delete a note")
    print("4-show some template requests or user request")
    print("5-show a statistics")
    print("6-exit the programm")
    print()

    print()

    method = input("Choose a method:")

    print("You choosed method", method)

    if method == "1":
        method_1(db_cursor, db_connection)

    elif method == "2":
        method_2(db_cursor, db_connection)

    elif method == "3":
        method_3(db_cursor, db_connection)

    elif method == "4":
        method_4(db_cursor, db_connection)

    elif method == "5":
        method_5(db_cursor, db_connection)

    elif method == "6":
        run = False

    elif method:
        print()
        print("A wrong method! Please, try again")
        print()
    print()