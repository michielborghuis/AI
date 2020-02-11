import random

min_getal = int(input('Wat mag de minimale waarde van het getal zijn? '))
max_getal = int(input('Wat mag de maximale waarde van het getal zijn? '))
getal = random.randrange(min_getal, max_getal+1)
guess = int(input('Kies een getal tussen de {} en de {}: '.format(min_getal, max_getal)))
while getal != guess:
    print('Helaas, uw gok was niet correct.')
    guess = int(input('Kies een getal tussen de {} en de {}: '.format(min_getal, max_getal)))
print('Je hebt het getal geraden!!!')