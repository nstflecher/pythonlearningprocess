# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 00:46:13 2018

@author: perso
"""

from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())