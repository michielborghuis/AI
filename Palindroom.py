string = 'Hello world!!!'


def palindroom1(string):
    palin = string[::-1]
    return palin

def palindroom2(string):
    palin = ''
    i = len(string)
    while i > 0:
        palin += string[i-1]
        i -= 1
    return palin


print(palindroom1(string))
print(palindroom2(string))