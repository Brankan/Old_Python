
a,b=input('Type city:city   -').split(':')

citysconnect={1:'Paris:London',2:'London:Warszawa'}

for x in citysconnect.items():

    print(x[1])
    if a+':'+b ==x[1]:
        raise Exception("Already exist")
numb=len(citysconnect)+1
adde=a+':'+b
citysconnect[numb]=adde

print(citysconnect)

from1,to2 =input('Type city:city   -').split(':')

for x in citysconnect.items():
    print(x)



