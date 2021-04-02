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

        utility_matrix = dataset.pivot_table(values=, index=, columns=, fill_value=0)

        X = utility_matrix.T

        return X

 
    def model_run(self, X):

        SVD = TruncatedSVD(n_components=5)

        decomposed_matrix = SVD.fit_transform(X)

        correlation_matrix = np.corrcoef(decomposed_matrix)
        
        return correlation_matrix


    def clean(self):

       

        self.data_prep = self.model_prep(self.data)

        self.data_output = self.model_run(self.data_prep)

      

    def get_recommendations(self, i, reg):