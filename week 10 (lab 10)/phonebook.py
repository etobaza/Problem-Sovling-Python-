import psycopg2
import psycopg2.extras
import csv

hostname = 'localhost'
database = 'ppbase'
username = 'postgres'
passwrd = 'darkside'
conn = None

try:
    with psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=passwrd) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            command = ''
            create_script = ''' 
                                    CREATE TABLE IF NOT EXISTS phonebook 
                                    (
                                    phone  varchar,
                                    name   varchar 
                                    ) '''

            cur.execute(create_script)
            cur.execute('SELECT * FROM phonebook')
            for record in cur.fetchall():
                print(record['name'], record['phone'])

            def changeNumber():
                namechange = input("Choose name to change number: ")
                nametonum = input("Enter number: ")
                script_namesonum = 'UPDATE phonebook SET phone = (%s) WHERE name = (%s)'
                cur.execute(script_namesonum, (nametonum, namechange))


            def addNumber():
                name = input('Name: ')
                number = input('Number: ')
                insert_script = 'INSERT INTO phonebook (phone, name) VALUES (%s, %s)'
                cur.execute(insert_script, (number, name))


            def addFromCsv():
                names = []
                numbers = []
                with open('week 10 (lab 10)/users.csv', newline='') as csvFile:
                    file_reader = csv.reader(csvFile, delimiter=",")
                    for row in file_reader:
                        names.append(row[0])
                        numbers.append(row[1])
                for i in range(len(names)):
                    insert_script = 'INSERT INTO phonebook (phone, name) VALUES ( %s, %s)'
                    cur.execute(insert_script, (numbers[i], names[i]))



            def changeName():
                nameInTable = input("Enter the name you want to change: ")
                newName = input("Enter the new name: ")
                script_changeName = 'UPDATE phonebook SET name = (%s) WHERE name = (%s)'
                cur.execute(script_changeName, (newName, nameInTable))


            def deleteUser():
                delete_script = 'DELETE FROM phonebook WHERE name = (%s)'
                userToDelete = str(input('Enter the username: '))
                cur.execute(delete_script, (userToDelete,))


            while command != 'commit':
                command = input('commands: commit, changenumber, changename, addnumber, csv, deleteuser \n')
                if command == 'changenumber':
                    changeNumber()
                elif command == 'addnumber':
                    addNumber()
                    id += 1
                elif command == 'csv':
                    addFromCsv()
                elif command == 'changename':
                    changeName()
                elif command == 'deleteuser':
                    deleteUser()
            conn.commit()
            cur.execute('SELECT * FROM phonebook')
            for record in cur.fetchall():
                print(record['name'], record['phone'])
except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()