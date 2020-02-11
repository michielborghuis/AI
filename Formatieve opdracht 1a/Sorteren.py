lst = [3, 9, 6, 8, 2, 9, 5, 2, 3, 3, 3]


def sort(lst):
    for i in range(len(lst)):
        for i in range(0, len(lst)-1):
            e = i+1
            if lst[i] > lst[e]:
                lst[i], lst[e] = lst[e], lst[i]
            else:
                continue
    return lst


print(sort(lst))