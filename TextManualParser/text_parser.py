# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 16:55:30 2020

@author: Mario Palazuelos - Aliado Analítico, Morelos, México
"""

class TextParser:
    
    def __init__(self, DATAFRAME, INDEX, COLUMN, TAG):
        
        #Creating the Objects that will build the Class Skeleton.
        self.DATAFRAME = DATAFRAME
        self.INDEX = INDEX
        self.COLUMN = COLUMN
        self.TAG = TAG
        
        #Create the "TAG" Column Object to use later with the Tagger Function
        self.DATAFRAME[TAG] = 0
        
        #Creating the Cell Object to impute functions
        self.CELL = self.DATAFRAME.loc[self.INDEX, self.COLUMN]
        
        
        

        #Forward function forwards to the next cell from current INDEX
    def Forward(self):
        self.INDEX = self.INDEX + 1
        self.CELL = self.DATAFRAME.loc[self.INDEX, self.COLUMN]
        
        
        
        
        #Backward function goes back to previous cell from current INDEX
    def Backward(self):
        self.INDEX = self.INDEX - 1
        self.CELL = self.DATAFRAME.loc[self.INDEX, self.COLUMN]
        
    
    
    
        #Tagger function tags the current cell with the users input
    def Tagger(self):
        self.DATAFRAME.loc[self.INDEX, self.TAG] = input()
        
        
        
        #Save funtion that saves the processed DF to a CSV File
    def Save(self, SAVEPATH):
        self.DATAFRAME.to_csv(f"{SAVEPATH}")
    
    
    
    
        #Clears the console
    def Clear(self):
        return print("\n"*10)
        