import mysql.connector as mysql

def create_database():
    mydb = mysql.connect(
        host="localhost",
        user="root",
        passwd='Michiel1805'
    )
    mycursor = mydb.cursor()

    mycursor.execute("DROP DATABASE IF EXISTS huwebshop")
    mycursor.execute("CREATE DATABASE huwebshop")


def create_table():
    mydb = mysql.connect(
        host="localhost",
        user="root",
        passwd='Michiel1805',
        database="huwebshop"
    )

    cur = mydb.cursor()

    cur.execute("DROP TABLE IF EXISTS products CASCADE")
    cur.execute("DROP TABLE IF EXISTS profiles CASCADE")
    cur.execute("DROP TABLE IF EXISTS profiles_previously_viewed CASCADE")
    cur.execute("DROP TABLE IF EXISTS sessions CASCADE")

    # All product-related tables

    cur.execute("""CREATE TABLE products
                    (id VARCHAR(255) PRIMARY KEY,
                     name VARCHAR(255),
                     brand VARCHAR(255),
                     type VARCHAR(255),
                     category VARCHAR(255),
                     subcategory VARCHAR(255),
                     subsubcategory VARCHAR(255),
                     targetaudience VARCHAR(255),
                     msrp INTEGER,
                     discount INTEGER,
                     sellingprice INTEGER,
                     deal VARCHAR(255),
                     description VARCHAR(10000));""")

    # All profile-related tables

    cur.execute("""CREATE TABLE profiles
                    (id VARCHAR(255) PRIMARY KEY,
                     latestactivity TIMESTAMP,
                     segment VARCHAR(255));""")

    cur.execute("""CREATE TABLE profiles_previously_viewed
                    (profid VARCHAR(255),
                     prodid VARCHAR(255));""")

    # All session-related tables

    cur.execute("""CREATE TABLE sessions
                    (id VARCHAR(255) PRIMARY KEY,
                     profid VARCHAR(255),
                     segment VARCHAR(255),
                     sale BOOLEAN,
                     starttime TIMESTAMP,
                     endtime TIMESTAMP,
                     duration INTEGER,
                     os VARCHAR(255),
                     devicefamily VARCHAR(255),
                     devicetype VARCHAR(7));""")

    cur.close()

def run():
    create_database()
    create_table()

run()