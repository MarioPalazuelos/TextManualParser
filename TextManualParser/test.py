# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 16:59:52 2020

@author: mpala
"""

import pandas as pd

from text_parser import TextParser


df = pd.read_csv("test_text.txt", header=None, names=['Gina'])
i = 0
column = 'Gina'


# Prueba Forward y Backward
check = TextParser(df,i, column, 'Tag')
# print(check.CELL)
# # check = TextParser(df,i, column).Forward()
# check.Forward()
# print(check.CELL)

# check.Backward()
# print(check.CELL)

# check.Backward()
# print(check.CELL)

# #Prueba Tagger
# check.Tagger()
# check.Forward()
# check.Tagger()
# check.Forward()