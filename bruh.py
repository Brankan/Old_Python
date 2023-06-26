ta=input('bruh:')
tab=[]
for x in ta:
    if x =='1':
        tab.append(1)
    if x =='2':
        tab.append(2)
    if x =='3':
        tab.append(3)
    if x =='4':
        tab.append(4)
    if x =='5':
        tab.append(5)
    if x =='6':
        tab.append(6)
    if x =='7':
        tab.append(7)
    if x =='8':
        tab.append(8)
    if x =='9':
        tab.append(9)
    if x =='0':
        tab.append(0)
tabb=[]
for okand in range(int(len(tab)/2)):
    tabb.append([tab[0],tab[1]])
    tab.remove(tab[0])

    tab.remove(tab[0])

print(tabb)

h=range(0, len(tab)+1, 2)
print(h)
