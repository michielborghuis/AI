def count():
    lst = [3, 9, 6, 8, 2, 9, 5, 2, 3, 3, 3]
    number = int(input('geef een getal: '))
    counter = 0
    for i in lst:
        if i == number:
            counter += 1
    print(counter)

count()