import random

def list_maker():
    list_of_lists = []
    number_of_lists = int(input('Hoeveel lijsten wilt u? '))
    number_of_numbers_in_list = int(input('Hoeveel getallen wilt u per lijst? '))
    min_getal = int(input('Hoe klein mogen de getallen zijn? '))
    max_getal = int(input('Hoe groot mogen de getallen zijn? '))
    for i in range(number_of_lists):
        lst = []
        for j in range(number_of_numbers_in_list):
            lst.append(random.randrange(min_getal, max_getal+1))
        list_of_lists.append(lst)
    return list_of_lists

def average(list_of_lists):
    for lst in list_of_lists:
        som = 0
        aantal = 0
        for getal in lst:
            som += getal
            aantal += 1
        average = som/aantal
        return average

print(average(list_maker()))