# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 23:29:05 2020

@author: SUPERNOVA2813
"""

def Factorial(data):
    if(data==1):
        return 1
    else:
        return data*Factorial(data-1)
    
print(Factorial(5))