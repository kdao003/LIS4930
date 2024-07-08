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
        self.file = file
        self.data = None
        self.data_numeric = None

    def load_data(self):
        self.data = pd.read_csv(self.file, sep = '\t')
        print(f"Data loaded successfully from {self.file}")

    def get_data(self):
        if self.data is not None:
            return self.data
        else:
            print("Data has not been loaded")
            return None
    
    def filter_numeric_cols(self):
        self.data_numeric = self.data.select_dtypes(include = "number")
        return self.data_numeric
    
    def normalization_test(self):
        if self.data_numeric is not None:
            self.data_numeric.hist(bins = 30, figsize = (8,10))
            plt.show()
        else:
            print("No numeric data to create a histogram with.")
        
#Example
#Selecting file
#Creating Root Window

root = tk.Tk()
root.withdraw()

file = filedialog.askopenfilename()
        
#Running Functions
norm = DataNormalization(file)
norm.load_data()
norm.filter_numeric_cols()
norm.normalization_test()





















