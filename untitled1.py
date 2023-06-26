# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 13:58:59 2021

@author: student
"""

def insertionsort(tab):
    for i in range(1, len(tab)):
        Value = tab[i]
        Position = i
        while Position > 0 and tab[Position - 1] > Value:
            tab[Position] = tab[Position -1]
            Position = Position - 1
        tab[Position] = Value
    return tab
