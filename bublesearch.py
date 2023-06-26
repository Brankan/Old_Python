# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 10:09:18 2021

@author: student
1000000 object with random.randint(1, 1000000) =
"""
import random
import time

A=[1,3,2]
for x in range(1,10**6):
    A.append(random.randint(1, 1000000))

def bubble(array):
    length = len(array)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
print("Start sort,time:"+time.ctime())
print("")
print("")

bubble(A)
print("ok,time:"+time.ctime())