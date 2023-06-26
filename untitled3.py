# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 13:15:32 2021

@author: student
"""

def era (n):
    b1 = [1]
    b2 = []
    for i in  range(2, n):
        if i not in b2:
            b1.append(i)
            b2.extend(range(i*i, n+1, i))
    return (b1)
    

print(era(1900))