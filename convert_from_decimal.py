# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 21:03:49 2018

@author: perso
"""

def convert_from_decimal (number, base):
     multiplier, result = 1,0
     while number > 0:
          result += number%base*multiplier
          multiplier *= 10
          number = number//base
     return result

def test_convert_from_decimal():
     number, base = 9,2
     assert(convert_from_decimal（number,base)==1001)
     print('Tests passed!')

#%%
#！/usr/bin/python
# -*- coding:UTF-8 -*-

print （"你好，世界”）
