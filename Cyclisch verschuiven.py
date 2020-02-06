def cyclisch_verschuiven(ch, n):
    ch = str(ch)
    if n != 0:
        ch = ch[n:] + ch[:n]
    else:
        print('Voer een waarde boven of onder de 0 in om de bitjes te verschuiven.')
    return ch

print(cyclisch_verschuiven(1011000, 3))
print(cyclisch_verschuiven(1011100, -4))
print(cyclisch_verschuiven(1010101, 0))