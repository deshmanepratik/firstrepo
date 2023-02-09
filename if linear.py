# -*- coding: utf-8 -*-
"""
Created on Fri May  1 00:41:01 2020

@author: deshmanp
"""

a = 11
b = 10
#Function definations below
def prat(a):
    print ("a is greater : "+str(a))
    return a*a

def prat_2(b):
    print ("b is greater : "+str(b))
    return b*b

greater = prat(a) if a>b else prat_2(b)
print ("and square of greater value is : "+str(greater))