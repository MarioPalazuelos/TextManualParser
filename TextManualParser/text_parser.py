# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 16:55:30 2020

@author: mpala
"""

class TextParser:
    
    def __init__(self, DATAFRAME, INDEX, COLUMN, TAG):
        
        #Creating the variables and methods that will build the Class Skeleton.
        self.DATAFRAME = DATAFRAME
        self.INDEX = INDEX
        self.COLUMN = COLUMN
        self.TAG = TAG
        
        #Create the "TAG" column to use later with the Tagger Function
        self.DATAFRAME[TAG] = 0
        
        #Creating the Cell Object to impute functions
        self.CELL = self.DATAFRAME.loc[self.INDEX, self.COLUMN]
        


   
    def Forward(self):
        self.INDEX = self.INDEX + 1
        self.CELL = self.DATAFRAME.loc[self.INDEX, self.COLUMN]
        
    def Backward(self):
        self.INDEX = self.INDEX - 1
        self.CELL = self.DATAFRAME.loc[self.INDEX, self.COLUMN]
        
        
        
        