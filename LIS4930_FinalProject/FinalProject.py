#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 00:20:57 2024

@author: kendao
"""

import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog


class DataNormalization:
    def __init__(self, file):
        self.file = file_name
        self.data = None
        self.data_numeric = None

    def load_data(self):
        self.data = pd.read_csv(self.file_name, sep = '\t')
        print(f"Data loaded successfully from {self.file_name}")

    def get_data(self):
        if self.data is not None:
            return self.data
        else:
            print("Data has not been loaded")
            return None
    
    def filer_numeric_cols(self):
        self.data_numeric = self.data.select_dtypse(include = "number")
        return self.numeric_data
    
    def Normalization_Test(self):
        self.numeric_data.hist(bins = 30, figsize = (8,10))
        plt.show()
        
#Example
#Selecting file
#Creating Root Window

root = tk.Tk()
root.withdraw()

file_name = filedialog.askopenfilename()
        
#Running Functions
norm = DataNormalization(file_name)
norm.load_data()
norm.filer_numeric_cols()
norm.Normalization_Test()





















