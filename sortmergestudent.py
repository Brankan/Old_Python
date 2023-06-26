import math
a=int(input('#:'))
x=0
tab=[]
g = ''

while x !=a:
    tabb=[]

    while True:

        g=input('%:')
        if g =='-':
            break
        else:
            tabb.append(g)

    tab.append(tabb)
    x=x+1

def mergeSort(alist):

    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1


for x in range(len(tab)):
    listtosort = []
    for b in tab[x]:
        listtosort.append(float(b.split(' ')[2]))
    mergeSort(listtosort)
    listtosort.reverse()
    calc=math.ceil(len(tab)*0.1)
    lol=0

    for bf in listtosort:
        for b in tab[x]:
                if float(b.split(' ')[2]) ==bf:
                    tab[x].remove(b)
                    lol=lol+1
                    if lol <= calc:
                        print(b.split(' ')[0] +' '+b.split(' ')[1])

    print('-')
