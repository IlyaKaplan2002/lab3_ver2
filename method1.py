def method_1(db_cursor, db_connection):

    print("Here you can create a new note")

    db_cursor.execute("SHOW TABLES;")

    tables = []

    for table in db_cursor:
        print(table)
        table = list(table)
        table = "".join(table)
        tables.append(table)

    table = input("Choose table:")

    if table in tables:
        db_cursor.execute("SELECT*FROM " + table + ";")

        for note in db_cursor:
            print(note)

        db_cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name='" + table + "';")

        print("!!!You shouldn't enter pre-existing id values!!!")

        insert_value = []

        for note in db_cursor:
            note = list(note)
            note = "".join(note)
            value = input("Input value for " + note + ":")
            insert_value.append(value)
        
        insert_value = "', '".join(insert_value)

        creating = input("Do you want to insert values '" + insert_value + "'? (y/n)")

        while (creating not in ('y', 'n')):
            creating = input("Wrong input. Do you want to insert values '" + insert_value + "'? (y/n)")

        if creating == "y":
                db_cursor.execute("INSERT INTO " + table + " VALUES ('" + insert_value + "');")
            
                db_connection.commit()

                print("Changes commited!")

                print("New version of table:")

                db_cursor.execute("SELECT*FROM " + table + ";")

                for note in db_cursor:
                    print(note)
            
        elif creating == "n":
            print("Creation of the new note was cancelled!") 
    
    else:
        print()
        print("Wrong table!")

