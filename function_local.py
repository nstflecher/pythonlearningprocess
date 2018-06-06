# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 09:21:18 2018

@author: perso
"""


x=50 

def func(x):
     print('x is', x)
     x=2
     print('changed local to',x)
     
     
func(x)
print('x is still', x)



