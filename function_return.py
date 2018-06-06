# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 20:56:24 2018

@author: perso
"""

def maximum(x,y):
     if x>y:
          return x
     elif x==y:
          return 'The numbers are equal'
     else:
          return y
     
print(maximum(2,3))