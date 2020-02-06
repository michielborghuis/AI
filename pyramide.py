def piramide_for():
    lenght = int(input('Hoe groot? '))

    for i in range(lenght+1):
        print('*' * i)
    for i in range(lenght):
        print('*' * (lenght-i))

def piramide_while():
    lenght = int(input('Hoe groot? '))
    count = 1
    while count < lenght:
        print('*' * count)
        count += 1
    while count > 0:
        print('*' * count)
        count -= 1

piramide_for()
piramide_while()


#print(f'{mystring:>{size}}')