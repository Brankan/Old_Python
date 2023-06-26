a=int(input('#:'))
tabb=[]
for ok in range(a):
    a,g=input('prod:').split(' ')
    tabb.append([a,g])
klucz=int(input('#:'))


def insertionsort(tab):
    for i in range(1, len(tab)):
        Value = tab[i]
        Position = i
        while Position > 0 and tab[Position - 1] > Value:
            tab[Position] = tab[Position -1]
            Position = Position - 1
        tab[Position] = Value
    return tab

if klucz==1:
    okand=[]
    ok=[]
    for b in tabb:
        okand.append(int(b[1]))
    insertionsort(okand)

    for x in okand:
        for b in tabb:
            if int(x) ==int(b[1]):
                ok.append(b)
                tabb.remove(b)
    ok.reverse()

    for xy in ok:
        print(xy[0]+' '+xy[1])
if klucz==0:
    okand = []
    ok = []
    for b in tabb:
        okand.append(b[0])
    insertionsort(okand)

    for x in okand:
        for b in tabb:
            if x == b[0]:
                ok.append(b)
                tabb.remove(b)

    for xy in ok:
        print(xy[0]+' '+xy[1])
