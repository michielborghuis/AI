import pymongo
import mysql.connector as mysql
import csv


f = open("password.txt", "r")
password = f.readline()
f.close()


def create_database():
    mydb = mysql.connect(
        host="localhost",
        user="root",
        passwd=password
    )
    mycursor = mydb.cursor()
    mycursor.execute("DROP DATABASE IF EXISTS testjelle")
    mycursor.execute("CREATE DATABASE testjelle")
def create_table():
    mydb = mysql.connect(
        host="localhost",
        user="root",
        passwd=password,
        database="testjelle"
    )
    mycursor = mydb.cursor()
    mycursor.execute("DROP TABLE IF EXISTS profiles")
    mycursor.execute("CREATE TABLE profiles ("
                     "id VARCHAR(255) PRIMARY KEY,"
                     "name VARCHAR(255),"
                     "age VARCHAR(255))")


def show_tables():
    mydb = mysql.connect(
        host="localhost",
        user="root",
        passwd=password,
        database="testjelle"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)


def add_data():
    mydb = mysql.connect(
        host="localhost",
        user="root",
        passwd=password,
        database="testjelle"
    )
    mycursor = mydb.cursor()


    with open('test.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row)
            id=row[0]
            name=row[1]
            age=row[2]
            mycursor.execute('''INSERT INTO profiles(id,name,age)
                VALUES ('{}','{}','{}')'''.format(id,name,age))
            mydb.commit()



def run():
    create_database()
    create_table()
    show_tables()
    add_data()
run()