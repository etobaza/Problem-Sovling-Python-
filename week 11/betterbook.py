import psycopg2
import psycopg2.extras
import csv

hostname = 'localhost'
database = 'advphonebook'
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
                                    CREATE TABLE IF NOT EXISTS phonebk 
                                    (
                                    phone  varchar,
                                    name   varchar PRIMARY KEY
                                    ) '''

            cur.execute(create_script)
            cur.execute('SELECT * FROM phonebk')
            for record in cur.fetchall():
                print(record['name'], record['phone'])


            def pagination(offset, limit, row):
                if row == "phone":
                    sql="SELECT * FROM pagination_with_phone_order({},{})".format(offset,limit)
                else:
                    sql="SELECT * FROM pagination_with_name_order({},{})".format(offset,limit)
                cur = conn.cursor()
                cur.execute(sql)
                print(cur.fetchall())
                conn.commit()
                cur.close()

            def delete_user(row, value):
                if row == "phone":
                    sql="CALL  delete_user_by_num('{}')".format(value)
                else:
                    sql="CALL  delete_user_by_name('{}')".format(value)

                cur = conn.cursor()
                cur.execute(sql)
                conn.commit()
                cur.close()


            def append_one(user, phone):
                cur = conn.cursor()
                cur.execute('CALL append_user(%s,%s)',(user, phone))
                conn.commit()
                cur.close()

            def append_list(arr):
                for i in arr:
                    append_one(i[0], i[1])
            

            def patternOutput(pattern, row):
                if row == "phone":
                    sql="SELECT * FROM get_records_by_number_pattern('{}')".format(pattern)
                else:
                    sql="SELECT * FROM get_records_by_name_pattern('{}')".format(pattern)
                cur = conn.cursor()
                cur.execute(sql)
                print(cur.fetchall())
                conn.commit()
                cur.close() 


            def addFromCsv():
                names = []
                numbers = []
                with open('week 11\kgb.csv', newline='') as csvFile:
                    file_reader = csv.reader(csvFile, delimiter=",")
                    for row in file_reader:
                        names.append(row[0])
                        numbers.append(row[1])
                for i in range(len(names)):
                    insert_script = 'INSERT INTO phonebk (phone, name) VALUES ( %s, %s)'
                    cur.execute(insert_script, (numbers[i], names[i]))
            
            while command != 'commit':
                command = input('commands: commit, csv, deleteuser, pagination, appendone, appendlist, pattern \n')
                if command == 'csv':
                    addFromCsv()
                elif command == 'deleteuser':
                    row = input("Enter collumn name: ")
                    value = input("Enter value: ")
                    delete_user(row, value)
                elif command == 'pagination':
                    offset = int(input("Enter offset: "))
                    limit = int(input("Enter limit: "))
                    row = input("Enter collumn name: ")
                    pagination(offset, limit, row)
                elif command == 'appendone':
                    user = input()
                    phone = input()
                    append_one(user, phone)
                elif command == 'appendlist':
                    append_list([('Meruyert', '+77082132323'), ('Slava', '+13372281488')])
                elif command == 'pattern':
                    pattern = input()
                    row = input()
                    patternOutput(pattern, row)

            conn.commit()
            cur.execute('SELECT * FROM phonebk')
            for record in cur.fetchall():
                print(record['name'], record['phone'])
except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()