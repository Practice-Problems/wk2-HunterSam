from math import *
def squares(a, b):
    ini = a
    chak = 0
    count = 0
    while (ini<=b):
        if ini**(1/2) == int(ini**(1/2)):
            chak = ini**(1/2) + 1
            count += 1
            break
        ini += 1
    while (ini <= b):
        if chak**2 <= b:
            count += 1
        else:
            return count
        chak += 1
    return count
#print(squares(10,1000))
def encryption(s):
    noSpace = s.replace(' ','')
    L = len(noSpace)
    up = int(ceil(sqrt(L)))
    lo = int(floor(sqrt(L)))
    out = ''
    for i in range(0,up):
        for j in range(i, L,up):
            out = out + noSpace[j]
        out += ' '
    return out.strip(' ')

#print(encryption('hello pakistan'))