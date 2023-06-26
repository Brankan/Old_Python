amount = float(input('amount = '))
types=input('types = ')
nominalss=types.split(',')
nominals=[]
for b in nominalss:
    nominals.append(float(b))
nominals=sorted(nominals,reverse=True)
output = {}
for n in nominals:
	output[n] = amount // n
	amount %= n
ok=[]
for k, v in output.items():
    for x in range(int(v)):
        ok.append(k)
print(len(ok),ok)
