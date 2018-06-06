# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 14:35:24 2018

@author: perso
"""

number=23
guess = int(input('Enter an integer:'))

if guess == number:
     #新的模块从这里开始
     print('Congratulations, you guessed it.')
     print('(but you do not win any prizes!)')
     #欣快在这里开始

elif guess<number:
     # 另一块代码
     print（'No,it is a little higher than that')
     # 你可以在此做任何你希望在改代码块内进行的事情
     
else:
     print('No, it is a little lower than that')
     # 你必须通过猜测一个大于(>)设置书的数字来到这里  