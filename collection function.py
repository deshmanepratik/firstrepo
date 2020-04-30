# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 23:52:19 2020

@author: deshmanp
"""
def prat(a):
    print("number is :"+str(a))
    b = a*a
    print("square is :"+str(b))

domain = [1, 2, 3, 4]

results = map(prat, domain)
print (list(results))