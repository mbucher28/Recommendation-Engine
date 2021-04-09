# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 15:29:52 2021

@author: mbucher
"""

import numpy as np

import pandas as pd

from sklearn.decomposition import TruncatedSVD

 

class Model:

 
    def __init__(self):

        self.data=pd.read_excel('datafile')
        self.clean()
 

    def model_prep(self, dataset):

        #instantiate model and prepare data for model

        return X

 
    def model_run(self, X):
        #Train model with prepared data
        
        
        return model_output


    def clean(self):

       

        self.data_prep = self.model_prep(self.data)

        self.model_output = self.model_run(self.data_prep)

      

    def get_recommendations(self, i, reg):
        #Feed input from GUI into trained model
        #Create output in desired  format