# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 23:52:19 2020

@author: deshmanp
"""
from functools import reduce
def prat(a):
    print("number is :"+str(a))
    b = a*a
    print("square is :"+str(b))
    return b;

def prat_2(a,b):
    print("number is :"+str(a)+"and " +str(b))
    print ("multiplication is " +str(a*b))
    return a*b

domain = [2, 2, 2, 2, 2, 2, 2, 2]

results = reduce(prat_2, domain, 1)
print("completed")
print (results)