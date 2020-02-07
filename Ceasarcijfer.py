def ceasarcijfer():
    alp_low = 'abcdefghijklmnopqrstuvwxyz'
    alp_upp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    text = input('Geef een tekst: ')
    rotation = int(input('Geef een rotatie: '))
    ceasarcode = ''
    for i in text:
        if i in alp_low:
            ceasarcode += alp_low[(alp_low.index(i)+rotation) % 26]
        elif i in alp_upp:
            ceasarcode += alp_upp[(alp_upp.index(i) + rotation) % 26]
        else:
            ceasarcode += i
    print('Ceasarcode: ' + ceasarcode)

print(ceasarcijfer())