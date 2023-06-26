# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 10:47:56 2021

@author: student
1000000 object with random.randint(1, 1000000)= 7 sec
10**8 object with random.randint(1, 1000000) =
"""

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


import random 
import time
A=[1,3,2]
for x in range(1,10**8):
    A.append(random.randint(1, 1000000))

print("Start sort,time:"+time.ctime())
print("")
print("")
mergeSort(A)
print("ok,time:"+time.ctime())
