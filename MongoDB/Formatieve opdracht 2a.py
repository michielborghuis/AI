import pymongo

client = pymongo.MongoClient('localhost', 27017)
database = client['huwebshop']
collection1 = database['products']
collection2 = database['profiles']
collection3 = database['sessions']

def first_product():
    print('Opdracht 1:')
    results = collection1.find({})
    for result in results[:1]:
        print(result["name"])
        print(result["price"])


def first_product_R():
    print('\n\nOpdracht 2:')
    results2 = collection1.find({"name": {'$regex': '^R'}})
    for result in results2[:1]:
        print(result["name"])


def average_price():
    print('\n\nOpdracht 3:')
    results3 = collection1.find({})
    sum_prices = 0
    count_prices = 0
    for result in results3:
        try:
            price = result['price']['selling_price']
            sum_prices += price
            count_prices += 1
        except:
            continue
    average_price = sum_prices/count_prices
    print(average_price)

def run():
    first_product()
    first_product_R()
    average_price()

run()