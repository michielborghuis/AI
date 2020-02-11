lst1 = [3, 9, 6, 8, 2, 9, 5, 2, 3, 3, 3]
lst2 = [1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1,
       1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0]

def count(lst, number):
    counter = 0
    for i in lst:
        if i == number:
            counter += 1
    return(counter)

def difference(lst):
    diff2 = 0
    for i in range(0, len(lst)-1):
        if lst[i] > lst[i+1]:
            diff = lst[i] - lst[i+1]
        else:
            diff = lst[i+1] - lst[i]
        if diff > diff2:
            diff2 = diff
    return(diff2)

def ones_and_zeros(lst, number0, number1):
    count0 = count(lst, number0)
    count1 = count(lst, number1)
    if count0 < 13 and count1 > count0:
        return 'De lijst voldoet aan de voorwaarden!'
    else:
        return 'De lijst voldoet niet aan de voorwaarden!'

print(count(lst1, int(input('Geef een getal: '))))
print(difference(lst1))
print(ones_and_zeros(lst2, 0, 1))