mydb = mysql.connect(
        host="localhost",
        user="root",
        passwd=password,
        database="huwebshop"
    )
    mycursor = mydb.cursor()
    mycursor.execute("DROP TABLE IF EXISTS recommendation")

    mycursor.execute("CREATE TABLE recommendation ("
                     "profid VARCHAR(255),"
                     "recProd1 VARCHAR(255),"
                     "recProd2 VARCHAR(255),"
                     "recProd3 VARCHAR(255),"
                     "recProd4 VARCHAR(255))")