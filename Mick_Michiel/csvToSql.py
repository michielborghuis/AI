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


    with open('brands.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            id=row[0]
            brand=row[1]
            mycursor.execute('''INSERT INTO brands(id, brand)
                VALUES ('{}','{}')'''.format(id,brand))
            mydb.commit()

    alreadyadded = []
    with open('doelgroepen.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            id=row[0]
            if id in alreadyadded:
                print("ok")
                pass
            else:
                doelgroep = row[1]
                if doelgroep == "Baby's":
                    doelgroep = "Baby''s"
                print("voeg toe id:" + str(id))

                mycursor.execute('''INSERT INTO doelgroepen(id, doelgroep)
                    VALUES ('{}','{}')'''.format(id, doelgroep))
                mydb.commit()
                alreadyadded.append(id)

    with open('genders.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            id=row[0]
            gender=row[1]
            mycursor.execute('''INSERT INTO genders(id,gender)
                VALUES ('{}','{}')'''.format(id,gender))
            mydb.commit()

    with open('categories.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            id=row[0]
            cat=row[1]
            mycursor.execute('''INSERT INTO categories(id,cat)
                VALUES ('{}','{}')'''.format(id,cat))
            mydb.commit()

def run():
    add_data()
run()