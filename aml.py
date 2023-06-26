import math
import matplotlib.pyplot as plt

k,m,A=input('ok:').split(' ')

k=int(k)
m=int(m)
A=int(A)
w=math.sqrt(k/m)
rez=[]
originf=[]
for xd in range(-200,200):
    originf.append(xd)
    tp=A*math.sin(w*xd)
    rez.append(tp)
print(rez)

plt.plot(originf, rez,label='fun' )
plt.axis([-100, 100, -100, 100])
plt.axhline(0, color='red')
plt.axvline(0, color='blue')
plt.show()

