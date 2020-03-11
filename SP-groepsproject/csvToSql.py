import mysql.connector as mysql
import csv


f = open("password.txt", "r")
password = f.readline()
f.close()


def add_data():
    mydb = mysql.connect(
        host="localhost",
        user="root",
        passwd=password,
        database="webshop"
    )
    mycursor = mydb.cursor()


    with open('profiles.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            id=row[0]
            segment=row[1]
            mycursor.execute('''INSERT INTO profiles(id,segment)
                VALUES ('{}','{}')'''.format(id,segment))
            mydb.commit()

    with open('buid.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            buid=row[0]
            profiles_id=row[1]
            mycursor.execute('''INSERT INTO buids(buid, profiles_id)
                VALUES ('{}','{}')'''.format(buid, profiles_id))
            mydb.commit()

    with open('sessions.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            id=row[0]
            segment=row[1]
            has_sale=row[2]
            buids_buid=row[3]
            mycursor.execute('''INSERT INTO profiles(id,segment,has_sale,buids_buid)
                VALUES ('{}','{}')'''.format(id,segment,has_sale,buids_buid))
            mydb.commit()

def run():
    add_data()
run()