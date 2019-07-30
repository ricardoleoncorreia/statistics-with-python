# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 18:07:31 2019

@author: FQ538HD
"""

import numpy as np
import scipy.stats as st

class CargoData:
    
    def __init__(self):
        self.std = 0
        self.mean = 0
        
    def get_safety_probability(self, cargo, n):
        mean_weight = cargo / n
        sample_std = self.std / np.sqrt(n) # Central limit theorem
        sample_mean = self.mean # Central limit theorem
        z = (mean_weight - sample_mean) / sample_std
        return 100 * st.norm.cdf(z)
    
    def set_data(self, std, mean):
        self.std = std
        self.mean = mean
        