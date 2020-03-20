import mysql.connector as mysql
import re
from psycopg2 import sql


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
    mycursor.execute("SELECT {} FROM {} WHERE {} LIKE {}".format(column, table, column2, like))
    result = mycursor.fetchone()
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
    _id = query_maker_like('prodid', 'profiles_previously_viewed', 'profid', profile)
    _id = string_to_integers(_id)
    return _id


profile_product('5a393d68ed295900010384ca')

def product_category(id):
    category = query_maker_like('category', 'products', 'id', str(id))
    print(remove_bad_chars(category))
    return remove_bad_chars(category)


product_category(45281)


def recommend_1():
    recommmendation_dict = {}
    profiles = profiles()
    for profile in profiles:
        recommendations = []
        product_id = profile_product(profile)
        category = product_category(product_id)




# profile()
#
# def run():
#     product_category()
# run()