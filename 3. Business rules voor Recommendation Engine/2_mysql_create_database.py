import mysql.connector as mysql


def create_database():
    mydb = mysql.connect(
        host="localhost",
        user="root",
        passwd='Michiel1805'
    )
    mycursor = mydb.cursor()

    mycursor.execute("DROP DATABASE IF EXISTS webshop")
    mycursor.execute("CREATE DATABASE webshop")


def create_table():
    mydb = mysql.connect(
        host="localhost",
        user="root",
        passwd='Michiel1805',
        database="webshop"
    )
    mycursor = mydb.cursor()
    mycursor.execute("DROP TABLE IF EXISTS products")
    mycursor.execute("DROP TABLE IF EXISTS sessions")
    mycursor.execute("DROP TABLE if EXISTS profiles")

    mycursor.execute("CREATE TABLE profiles ("
                     "id VARCHAR(255) PRIMARY KEY,"
                     "segment VARCHAR(255))")

    mycursor.execute("CREATE TABLE buids ("
                     "buid VARCHAR(255) PRIMARY KEY,"
                     "profiles_id VARCHAR(255))")

    mycursor.execute("CREATE TABLE sessions ("
                     "id VARCHAR(255) PRIMARY KEY, "
                     "buids_buid VARCHAR(255), "
                     "segment VARCHAR(45), "
                     "has_sale BOOLEAN)")

    mycursor.execute("CREATE TABLE brands ("
                     "id INT PRIMARY KEY, "
                     "brand VARCHAR(45))")

    mycursor.execute("CREATE TABLE categories ("
                     "id INT PRIMARY KEY, "
                     "cat VARCHAR(45))")

    mycursor.execute("CREATE TABLE genders ("
                     "id INT PRIMARY KEY, "
                     "gender VARCHAR(45))")

    mycursor.execute("CREATE TABLE doelgroepen ("
                     "id INT PRIMARY KEY, "
                     "doelgroep VARCHAR(45))")

    mycursor.execute("CREATE TABLE products ("
                     "id INT PRIMARY KEY, "
                     "name VARCHAR(255), "
                     "selling_price INT, "
                     "discount INT, "
                     "herhaalaankopen BOOLEAN, "
                     "kleur VARCHAR(255), "
                     "descr VARCHAR(10000), "
                     "eenheid VARCHAR(255), "
                     "inhoud VARCHAR(255), "
                     "leeftijd VARCHAR(255), "
                     "serie VARCHAR(255), "
                     "soort VARCHAR(255), "
                     "sterkte VARCHAR(255), "
                     "tax VARCHAR(255), "
                     "weekdeal BOOLEAN, "
                     "size VARCHAR(255), "
                     "brand_id INT, "
                     "cat_id INT, "
                     "gender_id INT, "
                     "doelgroep_id INT)")

    # mycursor.execute("CREATE TABLE orders ("
    #                  "session_id VARCHAR(255),"
    #                  "product_id INT)")

    # mycursor.execute("CREATE TABLE events ("
    #                  "session_id VARCHAR(255),"
    #                  "product_id INT)")

def show_tables():
    mydb = mysql.connect(
        host="localhost",
        user="root",
        passwd='Michiel1805',
        database="webshop"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")

    for x in mycursor:
        print(x)


def run():
    create_database()
    create_table()
    show_tables()

run()