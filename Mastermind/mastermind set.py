lst1 = [1, 2, 3, 4, 5, 6]
lst2 = [1, 2, 3, 4, 5, 6]
lst3 = [1, 2, 3, 4, 5, 6]
lst4 = [1, 2, 3, 4, 5, 6]

lst = [[a, b, c, d] for a in lst1 for b in lst2 for c in lst3 for d in lst4]
print(lst)
counter = 0
for i in lst:
    counter += 1
print(counter)