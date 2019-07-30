# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 19:12:40 2019

@author: FQ538HD
"""

import numpy as np
import scipy.stats as st

class WallStreetData:
    
    def __init__(self):
        self.std = 0
        self.mean = 0
        
    def get_probability_of_profit_in_week(self, profit, n):
        mean_profit_per_trade = profit / n
        sample_std = self.std / np.sqrt(n) # Central limit theorem
        sample_mean = self.mean # Central limit theorem
        z = (mean_profit_per_trade - sample_mean) / sample_std
        return 100 * st.norm.cdf(z)
    
    def set_data(self, std, mean):
        self.std = std
        self.mean = mean
        