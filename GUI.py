# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 15:29:50 2021

@author: mbucher
"""

import tkinter as tk

from tkinter import ttk

 

 

class gui(tk.Tk):

   

    PAD= 75

   

    

    def __init__(self, controller):

       

        super().__init__()

       

        self.title('Recommendation Engine 1.0')

       

        self.controller= controller

       

        self.value_var = tk.StringVar()

        self.region_var = tk.StringVar()

        self.segment_var = tk.StringVar()

        self._makeLabel()

        self._makeMainFrame()

        self._makeEntry()

        self._region()

        self._segment()

        self._button()

       

    def main(self):

        self.mainloop()

  

    def _makeMainFrame(self):

        self.main_frm = ttk.Frame(self)

        self.main_frm.pack(padx=self.PAD, pady=self.PAD)

       

    def _makeLabel(self):

        label = ttk.Label(text= 'Enter a Product for Recommendation')

        label.pack()

    def _makeEntry(self):

        self.ent= ttk.Entry(self.main_frm, justify= 'right', textvariable=self.value_var)

        self.ent.pack()

    def _region(self):

        self.region= ttk.Combobox(self.main_frm, width= 27, textvariable = self.region_var)

        self.region['values']=()

        self.region.pack()

    def _segment(self):

        self.segment= ttk.Combobox(self.main_frm, width= 27, textvariable = self.segment_var)

        self.segment['values']=()

        self.segment.pack()

    def _button(self):

        btn=ttk.Button(self, text= 'Get recommendations', command=self.controller.on_button)

        btn.pack()
