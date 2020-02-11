def tekstcheck():
    str1 = input('Geef een string: ')
    str2 = input('Geef een string: ')
    if str1 < str2:
        str1, str2 = str2, str1
    for i in range(0, len(str1)):
        if str1[i] is not str2[i]:
            print('Het eerste verschil zit op index: ' + str(i))
            break

tekstcheck()