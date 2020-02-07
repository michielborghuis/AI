myfile = open('test123.txt', 'r')
newfile = open('new123.txt', 'a')
lines = myfile.readlines()
myfile.close()

for line in lines:
    if line == '\n':
        del line
    else:
        line = line.lstrip()
        newfile.write(line)
newfile.close()

#lstrip methode gevonden op https://stackoverflow.com/questions/959215/how-do-i-remove-leading-whitespace-in-python