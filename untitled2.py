# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 10:25:20 2021

@author: student
"""
x =int(input("0:"))
li=[]
def Fib(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]

    li = Fib(n-1)
    li.append(li[-1] + li[-2])
    return li
    

    
print(Fib(x))

    