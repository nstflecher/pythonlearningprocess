# -*- coding: utf-8 -*-
"""
Created on Sat May 26 12:44:26 2018

@author: perso
"""

#这个例子的目的是搜索子字符串，这个子字符串以hello 开始，后面跟着零个或几个制表符或空格，接着有任意字符并将其保存至匹配的group中，最后以world结尾，如果找到这样的子字符串，与模式中括号包含的部分匹配的子字符串的对应部分保存为组

import re
match = re.match('Hello[\t]*(.*)world', 'Hello Python world')
match.group(1)

#例如，下面的模式取出了三个被斜线所分割的组：
{x: ord(x) for x in 'spaam'}
