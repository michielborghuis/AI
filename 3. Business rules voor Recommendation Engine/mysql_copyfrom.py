import mysql.connector as mysql
import csv


def add_data_new():
    mydb = mysql.connect(
        host="localhost",
        user="root",
        passwd='Michiel1805',
        database="huwebshop"
    )
    mycursor = mydb.cursor()

    mycursor.execute("LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/products.csv'"
                     "INTO TABLE products"
                     "CHARACTER SET UTF8"
                     "COLUMNS TERMINATED BY ','"
                     "ENCLOSED BY '\"'"
                     "LINES TERMINATED BY '\n'"
                     "IGNORE 1 LINES")

    mycursor.execute("LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/profiles.csv'"
                     "INTO TABLE profiles"
                     "CHARACTER SET UTF8"
                     "COLUMNS TERMINATED BY ','"
                     """ENCLOSED BY '"'"""
                     "LINES TERMINATED BY '\n'"
                     "IGNORE 1 LINES"
                     "(id, @latestactivity, segment)"
                     "SET latestactivity = nullif(@latestactivity,'null')")

    mycursor.execute("LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/profiles_previously_viewed.csv'"
                     "INTO TABLE profiles_previously_viewed"
                     "CHARACTER SET UTF8"
                     "COLUMNS TERMINATED BY ','"
                     """ENCLOSED BY '"'"""
                     "LINES TERMINATED BY '\n'"
                     "IGNORE 1 LINES")

    mycursor.execute("LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/sessions.csv'"
                     "INTO TABLE sessions"
                     "CHARACTER SET UTF8"
                     "COLUMNS TERMINATED BY ','"
                     """ENCLOSED BY '"'"""
                     "LINES TERMINATED BY '\n'"
                     "IGNORE 1 LINES")

def add_data():
    mydb = mysql.connect(
        host="localhost",
        user="root",
        passwd='Michiel1805',
        database="huwebshop"
    )
    mycursor = mydb.cursor()


    with open('products.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            id=row[0]
            name=row[1]
            brand=row[2]
            type=row[3]
            category=row[4]
            subcategory=row[5]
            subsubcategory=row[6]
            targetaudience=row[7]
            msrp=row[8]
            discount=row[9]
            sellingprice=row[10]
            deal=row[10]
            description=row[11]

            mycursor.execute('''INSERT INTO products(id,name,brand,type,category,subcategory,subsubcategory,targetaudience,msrp,discount,sellingprice,deal,description)
                VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')'''.format(id,name,brand,type,category,subcategory,subsubcategory,targetaudience,msrp,discount,sellingprice,deal,description))
            mydb.commit()

    with open('profiles.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            id=row[0]
            latestactivity=row[1]
            segment=row[2]
            mycursor.execute('''INSERT INTO profiles(id,latestactivity,segment)
                VALUES ('{}','{}','{}')'''.format(id,latestactivity,segment))
            mydb.commit()

    with open('profiles_previously_viewed.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            profid=row[0]
            prodid=row[1]
            mycursor.execute('''INSERT INTO profiles_previous_viewed(profid,prodid)
                VALUES ('{}','{}')'''.format(profid,prodid))
            mydb.commit()

    with open('sessions.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            id=row[0]
            profid=row[1]
            segment=row[2]
            sale=row[3]
            starttime=row[4]
            endtime=row[5]
            duration=row[6]
            os=row[7]
            devicefamily=row[8]
            devicetype=row[9]
            mycursor.execute('''INSERT INTO sessions(id,profid,segment,sale,starttime,endtime,duration,os,devicefamily,devicetype)
                VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')'''.format(id,profid,segment,sale,starttime,endtime,duration,os,devicefamily,devicetype))
            mydb.commit()

add_data_new()