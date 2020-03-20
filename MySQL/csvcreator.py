from pymongo import MongoClient
import csv
import databasecreator
import unidecode

mongo_client = MongoClient('localhost', 27017)

db = mongo_client.huwebshop

ses_col = db.sessions # 3
prof_col = db.profiles # 2
prod_col = db.products # 1

ses_cur = ses_col.find().limit(1000)
prof_cur = prof_col.find().limit(1000)
prod_cur = prod_col.find().limit(1000)




def csvWriter(filename, list):
    try:
        with open(filename, "a", newline='') as file:
            inData = csv.writer(file, delimiter=',')
            inData.writerow(list)

    except:
        print(Exception)
        pass


def writecsv(name, possible_watdanook):
    with open(name, "a", newline='') as file:
        for i in possible_watdanook:
            value_list_watdanook = []
            value_list_watdanook.append(possible_watdanook.index(i))
            value_list_watdanook.append(i)
            inData = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            inData.writerow(value_list_watdanook)


def csvProfiles(data, filename):
    key_list = ['_id', 'recommendations']
    key_list_recommendations = ['segment']
    for profile in list(data):
        value_list = []
        for key in key_list:
            try:
                if key == 'recommendations':
                    for recommendations_key in profile[key]:
                        if recommendations_key in key_list_recommendations:
                            value_list.append(profile[key][recommendations_key])
                else:
                    value_list.append(profile[key])
            except:
                value_list.append('NULL')
        csvWriter(filename, value_list)


def csvProducten(data):
    key_list = ['_id', 'name', 'gender','category', 'brand', 'price', 'herhaalaankopen', 'color', 'properties', 'size']
    key_list_price = ['selling_price', 'discount']
    key_list_properties = ['eenheid', 'inhoud', 'leeftijd', 'serie', 'soort', 'sterkte', 'tax', 'weekdeal', 'doelgroep']
    possible_gender = []
    possible_brands = []
    possible_doelgroepen = []
    possible_categories = []
    for num, i in enumerate(list(data)):
        count = 0
        value_list = []
        for y in key_list:
            try:
                if y == 'brand':
                    if i[y] in possible_brands:
                        value_list.append(possible_brands.index(i[y]))
                        count += 1
                    else:
                        possible_brands.append(i[y])
                        value_list.append(possible_brands.index(i[y]))
                        count += 1
                elif y == 'gender':
                    if i[y] in possible_gender:
                        value_list.append(possible_gender.index(i[y]))
                        count+=1
                    else:
                        possible_gender.append(i[y])
                        value_list.append(possible_gender.index(i[y]))
                        count += 1
                elif y == 'category':
                    if i[y] in possible_categories:
                        value_list.append(possible_categories.index(i[y]))
                        count += 1
                    else:
                        possible_categories.append(i[y])
                        value_list.append(possible_categories.index(i[y]))
                        count += 1
                elif y == 'price':
                    for j in i[y]:
                        if j in key_list_price:
                            if i[y][j] == None:
                                value_list.append('NULL')
                            else:
                                value_list.append(i[y][j])
                            count += 1
                elif y == 'herhaalaankopen':
                    if i[y]:
                        value_list.append(1)
                        count += 1
                    else:
                        value_list.append(0)
                        count += 1

                elif y == 'properties':
                    for j in i[y]:
                        if j in key_list_properties:
                            if j == "doelgroep":
                                if i[y][j] in possible_doelgroepen:
                                    value_list.append(possible_doelgroepen.index(i[y][j]))
                                    count += 1
                                else:
                                    possible_doelgroepen.append(i[y][j])
                                    value_list.append(possible_doelgroepen.index(i[y][j]))
                                    count += 1
                            elif j == 'weekdeal':
                                if i[y][j]:
                                    value_list.append(1)
                                    count += 1
                                else:
                                    value_list.append(0)
                                    count += 1
                            else:
                                if type(i[y][j]) == str:
                                    new_string = unidecode.unidecode(i[y][j])
                                    value_list.append(new_string)
                                else:
                                    value_list.append(i[y][j])
                                    count += 1
                else:
                    if type(i[y]) == str:
                        new_string = unidecode.unidecode(i[y])
                        value_list.append(new_string)
                    else:
                        value_list.append(i[y])
            except:
                print(Exception)
                pass
        print(count)
        csvWriter('products.csv', value_list)

    writecsv("doelgroepen.csv", possible_doelgroepen)
    writecsv("genders.csv", possible_gender)
    writecsv("brands.csv", possible_brands)
    writecsv("categories.csv", possible_categories)


def csvSessies(data, filename):
    key_list = ['_id', 'buid', "segment", 'has_sale', 'order', 'events', 'sources']
    for num, i in enumerate(list(data)):
        value_list = []
        order_list = []
        source_list = []
        event_list = []
        buid_list = []
        for y in key_list:
            try:
                if y == '_id':
                    value_list.append(i[y])
                    order_list.append(i[y])
                    event_list.append(i[y])
                    source_list.append(i[y])
                    buid_list.append(i[y])

                elif y == 'has_sale':
                    if i[y]:
                        value_list.append(1)
                    else:
                        value_list.append(0)
                elif y == 'buid':
                    for j in i[y]:
                        buid_list.append(j)
                        value_list.append(j)
                elif y == 'order':
                    if i[y] is not None:
                        for j in i[y]:
                            for c in i[y][j]:
                                for m in c.values():
                                    order_list.append(m)
                        csvWriter('orders.csv', order_list)
                    else:
                        pass
                elif y == 'events':
                    for j in i[y]:
                        for c in j:
                            if c == 'product' and j[c] is not None:
                                event_list.append(j[c])
                    if len(event_list) > 1:
                        csvWriter('events.csv', event_list)
                elif y == 'sources':
                    for j in i[y]:
                        source_list.append(j['full_url'])
                    csvWriter('sources.csv', source_list)
                else:
                    try:
                        value_list.append(i[y])
                    except:
                        value_list.append('NULL')
            except:
                pass
        csvWriter(filename, value_list)
        csvWriter('buids.csv', buid_list)

def swap_buids():
    with open('buids.csv', 'r', newline='') as in_file_handle:
        reader = csv.reader(in_file_handle)
        content = []
        for row in reader:
            content.append([row[1]] + [row[0]] + row[2:])
        with open('buids.csv', 'w', newline='') as out_file_handle:
            writer = csv.writer(out_file_handle)
            writer.writerows(content)

csvSessies(ses_cur, 'sessions.csv')
csvProfiles(prof_cur, 'profiles.csv')
csvProducten(prod_cur)
swap_buids()