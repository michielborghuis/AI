def fibonaci(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fibonaci(index-1) + fibonaci(index-2)

print(fibonaci(9))