def method_4(db_cursor, db_connection):

    print("Here you can see some template requests or user request")
    print("Templates:")
    print("1-full Timetable for your subgroup")
    print("2-student list")
    print("3-list of theachers")
    print("4-user request or user changes")

    template = input("Select a template:")

    while template not in ('1', '2', '3', '4'):
        template = input("Wrong input. Select a template again:")
    
    if template == "1":

        subgroup = input("Enter your subgroup from (1, 2, 3):")

        while subgroup not in ('1', '2', '3'):
            subgroup = input("Wrong subgroup. Enter your subgroup again (1, 2 or 3:")

        db_cursor.execute("SELECT*FROM timetable_full WHERE subgroup=" + subgroup + ";")

        for note in db_cursor:
            print(note)

    elif template == "2":

        db_cursor.execute("SELECT*FROM students;")

        for note in db_cursor:
            print(note)
    
    elif template == "3":

        db_cursor.execute("SELECT*FROM teachers;")

        for note in db_cursor:
            print(note)
    
    elif template == "4":
        try:
            request = input("Please input a right request/changes for MySQL syntax: ")

            confirm = input("Do you want to confirm your request/changes: '" + request + "'? (y/n)")

            while (confirm not in ('y', 'n')):
                confirm = input("Wrong input. Do you want to confirm your request/changes: '" + request + "'? (y/n)")

            if confirm == "y":
                db_cursor.execute(request)

                for note in db_cursor:
                    print(note)
                
                db_connection.commit()
                
            elif confirm == "n":
                print("Requst/Changes was cancelled")
        
        except:
            print()
            print("Wrong request!")