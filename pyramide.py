lenght = int(input('Hoe groot? '))

for i in range(lenght+1):
    print('*' * i)
for i in range(lenght):
    print('*' * (lenght-i))