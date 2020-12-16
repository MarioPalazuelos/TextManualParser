# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 16:59:52 2020

@author: mpala
"""

import pandas as pd

from text_parser import TextParser


df = pd.read_csv("test_text.txt", header=None)
i = 1
check = TextParser(df,i)