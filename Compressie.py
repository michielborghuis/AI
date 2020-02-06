def compressie():
    infile = open('test123.txt', 'r')
    content = infile.read()
    infile.close()

    compressie = content.strip()
    print(compressie)

print(compressie())