# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 15:29:43 2021

@author: mbucher
"""

from GUI import gui
from Recommendation import Model


class controller:

   
    def __init__(self):

        self.model=Model()

        self.view=gui(self)

      
    def main(self):

        self.view.main()

       
    def on_button(self):

        product=self.view.ent.get()

        region= self.view.region.get()

        self.model.get_recommendations(product, region)

        print(region)

   
if __name__ == '__main__':

    recommend = controller()

    recommend.main()

 

 

 
