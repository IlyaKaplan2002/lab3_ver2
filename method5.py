def method_5(db_cursor, db_connection):

    print("Here you can see some statistics")
    print("1-amount of students in subgroup")
    print("2-amount of pairs of your subgroup in the day")

    statistics = input("Choose a statistics(1, 2):")

    while statistics not in ('1', '2'):
        statistics = input("Wrong number of statistics. Choose another(1 or 2):")
    
    if statistics == '1':
        subgroup = input("Enter your subgroup (1, 2, 3):")

        while subgroup not in ('1', '2', '3'):
            subgroup = input("Wrong subgroup. Enter your subgroup again (1, 2 or 3):")
        
        db_cursor.execute("SELECT COUNT(*) FROM students WHERE subgroup=" + subgroup)

        print()

        for note in db_cursor:
            note = list(note)
            note = str(note)
            note = "".join(note)
            print("Amount of students in subgrop " + subgroup + " is " + note)
            print()
    
    if statistics == '2':
        subgroup = input("Enter your subgroup (1, 2, 3):")

        while subgroup not in ('1', '2', '3'):
            subgroup = input("Wrong subgroup. Enter your subgroup again (1, 2 or 3):")
        
        day = input("Enter a day (monday, tuesday, wednesday, thursday, friday):")

        while day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday'):
            day = input("Wrong day. Enter your subgroup again (monday, tuesday, wednesday, thursday, friday):")

        db_cursor.execute("SELECT COUNT(*) FROM timetable_full WHERE subgroup='" + subgroup + "' AND day='" + day + "';")

        print()

        for note in db_cursor:
            note = list(note)
            note = str(note)
            note = "".join(note)
            print("Amount of pairs in subgrop " + subgroup + " in " + day + " is " + note)
            print()