# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 09:25:42 2018

@author: perso
"""

#可变参数
def total(a=5, *numbers, **phonebook):
     print('a',a)
     
     #遍历元祖中的所有项目
     for single_item in numbers:
         print('single_item', single_item)
     
     #遍历字典中的所有项目
     for first_part, second_part in phonebook.items():
           print(first_part, second_part)
           
print(total(10,1,2,3, Jack=1123, John=2231, Inge=1560))



#他是如何工作的
#当我们声明一个诸如*param 的星号参数时，从此处开始直到结束的所有位置参数(positional Arguments)
#都将被收集并汇集成一个成为param 的元祖(Tuple)。
#类似的，当我们声明一个诸如**param 的双星号参数时候，从此处开始直到结束的所有关键字参数都将被收集并汇集成一个名为param的字典(Dictionary)
#我们将在后面的章节探索有关元祖和字典的更多内容
 



