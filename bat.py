b=int(input('type count:'))

oddziału=[]
pracowniki=[]
freepracowniki=[]
idprac=[]

def nazwaOddziału_wielkośćZmiany(first,second):
    b=first+":"+second
    oddziału.append(b)

def nazwaPracownika_nazwaOddziału(first,second):
    if second=='0':
        freepracowniki.append(first)
        idprac.append(first)


        return ''

    a=-1
    for x in oddziału:
        a+=1
        b=x.split(':')
        if b[0]==second:
            if a<len(pracowniki):
                insert=pracowniki[a]+','+first
                pracowniki.remove(pracowniki[a])
                pracowniki.insert(a,insert)
                idprac.append(first)
            if a>=len(pracowniki):
                pracowniki.insert(a, first)
                idprac.append(first)


def nazwaOddziału(first):
    a=-1
    for x in oddziału:
        a += 1
        b = x.split(':')
        if b[0] == first:
            freepracowniki.append(pracowniki[a])
            pracowniki.remove(pracowniki[a])
            oddziału.remove(x)



def idPracownika_nazwaOddziału(first,second):
    nazwa=idprac[int(first)]
    print(nazwa)
    for y in pracowniki:
        l = y.split(',')
        for b in l:
            if b==nazwa:
                l.remove(b)
                ff=','.join(l)
                pracowniki.insert(pracowniki.index(y),str(ff))
                pracowniki.remove(y)

                a = -1
                for x in oddziału:
                    a += 1
                    b = x.split(':')
                    if b[0] == second:
                        if a < len(pracowniki):
                            insert = pracowniki[a] + ',' + nazwa
                            pracowniki.remove(pracowniki[a])
                            pracowniki.insert(a, insert)
                        if a >= len(pracowniki):
                            pracowniki.insert(a, nazwa)
                return ''




def idPracownika_nazwaPracownika(first,second):
    for x in freepracowniki:
        if x==idprac[first]:
            freepracowniki.remove(idprac[first])
            freepracowniki.append(second)

    a = -1
    for b in pracowniki:
        a += 1
        inpact=''
        f=b.split(',')
        for k in f:
            if k == idprac[int(first)]:
                inpact += second +','
            else:
                inpact +=k+','

        pracowniki.remove(pracowniki[a])
        pracowniki.insert(a,inpact)

    idprac.remove(idprac[int(first)])
    idprac.insert(int(first),second)



def nazwaOddziału_nowaNazwaOddziału_nowaWieklośćZmiany(first,second,third):
    a=-1
    g=second+":"+third
    for x in oddziału:
        a += 1
        b = x.split(':')
        if b[0] == first:
            oddziału.remove(oddziału[a])
            oddziału.insert(a,g)

def fun(first):
    print(first)

while True:
    print('')
    a=input('Type:').split(' ')
    if a[0]=='a' and a[1]=='w':
        nazwaOddziału_wielkośćZmiany(a[2],a[3])
    if a[0]=='a' and a[1]=='e':
        nazwaPracownika_nazwaOddziału(a[2],a[3])
    if a[0] == 'd' and a[1] == 'w':
        nazwaOddziału(a[2])
    if a[0] == 'm':
        idPracownika_nazwaOddziału(a[1],a[2])
    if a[0] == 'e' and a[1] == 'e':
        idPracownika_nazwaPracownika(a[2],a[3])
    if a[0] == 'e' and a[1] == 'w':
        nazwaOddziału_nowaNazwaOddziału_nowaWieklośćZmiany(a[2], a[3], a[4])
    if a[0] == 's':
        fun(a[1])

