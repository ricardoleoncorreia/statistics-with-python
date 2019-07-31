# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 12:16:03 2019

@author: FQ538HD
"""

import numpy as np
import scipy.stats as st

class BookData:
    
    def __init__(self):
        self.mean = 0
        self.std = 0
    
    def two_tail_testing(self, n, new_mean, significance):
        sample_mean = self.mean # Central limit theorem
        sample_std = self.std / np.sqrt(n) # Central limit theorem
        z = (new_mean - sample_mean) / sample_std
        limit_range = (100 - significance) / 2
        probability = 100 * st.norm.cdf(z)
        val_str = 'not' if limit_range < probability < 1 - limit_range else ''
        print('Null hypothesis can{} be rejected (returned probability: {:0.2f}%)'.format(val_str, 100 - probability))
        
    def set_data(self, mean, std):
        self.mean = mean
        self.std = std
