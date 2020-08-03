# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 23:33:53 2020

@author: SUPERNOVA2813
"""
def Fibonnaci(data):
    if(data==1):
        return 0
    if data==2:
        return 1
    else:
        return Fibonnaci(data-1) + Fibonnaci(data-2) 

print(Fibonnaci(9))