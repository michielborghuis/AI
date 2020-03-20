import mysql.connector as mysql
import re
import csv


def csvWriter(filename, list):
    try:
        with open(filename, "a", newline='') as file:
            inData = csv.writer(file, delimiter=',')
            inData.writerow(list)

    except:
        print(Exception)
        pass


def string_to_integers(string):
    if type(string) != str:
        string = str(string)
    integers = re.sub('\D', '', string)
    return integers


def remove_bad_chars(string):
    if type(string) != str:
        string = str(string)
    new_string = re.sub('[\'\,\(\)\{\}<>]', "", string)
    return new_string


def query_maker_limit(column, table, limit):
    mydb = mysql.connect(
        host="localhost",
        user="root",
        passwd='Michiel1805',
        database='huwebshop'
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT {} FROM {} LIMIT {}".format(column, table, limit))
    result = mycursor.fetchall()
    return result


def query_maker_like(column, table, column2, like):
    mydb = mysql.connect(
        host="localhost",
        user="root",
        passwd='Michiel1805',
        database='huwebshop'
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT {} FROM {} WHERE {} LIKE '{}'".format(column, table, column2, like))
    result = mycursor.fetchone()
    return result


def query_maker_like_limit(column, table, column2, like, limit):
    mydb = mysql.connect(
        host="localhost",
        user="root",
        passwd='Michiel1805',
        database='huwebshop'
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT {} FROM {} WHERE {} LIKE '{}' LIMIT {}".format(column, table, column2, like, limit))
    result = mycursor.fetchall()
    return result


def profiles():
    profiles = []
    data = query_maker_limit('profid', 'profiles_previously_viewed', '10')
    for i in data:
        if remove_bad_chars(i) in profiles:
            continue
        else:
            profiles.append(remove_bad_chars(i))
    return profiles


def profile_product(profile):
    id = query_maker_like('prodid', 'profiles_previously_viewed', 'profid', profile)
    id = string_to_integers(id)
    return id


def product_category(id):
    category = query_maker_like('category', 'products', 'id', str(id))
    category = remove_bad_chars(category)
    return remove_bad_chars(category)


def recommend_1():
    for profile in profiles():
        valueList = []
        valueList.append(profile)
        product_id = profile_product(profile)
        category = product_category(product_id)
        recommendations = query_maker_like_limit('id', 'products', 'category', category, 4)
        for id in recommendations:
            valueList.append(string_to_integers(id))
        csvWriter('recommendation1.csv', valueList)


def run():
    recommend_1()


run()