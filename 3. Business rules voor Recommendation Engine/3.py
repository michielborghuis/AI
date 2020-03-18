import mysql.connector as mysql

def get_data():
    mydb = mysql.connect(
            host="localhost",
            user="root",
            passwd='Michiel1805',
            database='huwebshop'
        )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM products")
    data = mycursor.fetchall()
    print(data)

get_data()