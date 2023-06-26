# -*- coding: utf-8 -*-
"""
@author: Brankan


1000000 object with random.randint(1, 1000000) =5 sec 
10**8 object with random.randint(1, 1000000) =9 min
"""
import random 
import time
A=[9,11,10]
for x in range(1,10**8):
    A.append(random.randint(1, 1000000))



print("Start sort,time:"+time.ctime())
print("")
print("")

length = len(str(max(A)))
rang = 10
for i in range(length):
    B = [[] for k in range(rang)] 
    for x in A:
        figure = x // 10**i % 10
        B[figure].append(x)
    A = []
    for k in range(rang):
        A = A + B[k]
print("ok,time:"+time.ctime())
print(A)
