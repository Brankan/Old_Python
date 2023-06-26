# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 10:18:55 2021

@author: student
binarysearch
"""
"""
tab = [2,4,5,7,8]
el_tofind = 9
left = 0
right = len(tab)-1

while left <= right:
    mid = left+right
    
    if tab[mid]== el_tofind:
        print(mid)
        break
    elif tab[mid]<el_tofind:
        left=mid+1
    else:
        right =mid-1
else:
    print("Nie ma takiego elementu")
"""

ok=0

def Bin(lys, val,):
    global ok
    first=0
    last = len(lys)-1
    index = -1
    if (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
            return index+ok
        else:
            if val<lys[mid]:
                last = mid -1
                lys.remove(lys[mid])
                lys.remove(lys[])
            else:
                first = mid +1 
                lys.remove(lys[mid])
            ok +=1
            print(lys)

            return(Bin(lys, val))
            
        
    

print(Bin([1,2,3,4,6,222,7,10,12],12),'result')
