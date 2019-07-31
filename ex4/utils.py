# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 19:30:55 2019

@author: FQ538HD
"""

import numpy as np
import scipy.stats as st

class TvData:
    
    def __init__(self):
        self.std = 0
        self.mean = 0
        
    def hypothesis_testing_result(self, new_mean, n, alfa):
        sample_std = self.std / np.sqrt(n) # Central limit theorem
        sample_mean = self.mean # Central limit theorem
        z = (new_mean - sample_mean) / sample_std
        probability = 100 * st.norm.cdf(z)
        confidence = 100 - probability
        negation_string = '' if probability < 100 * alfa else 'not'
        result = 'Null hypothesis can{} be rejected ({:.2f}% confidence)'.format(negation_string, confidence)
        return result
    
    def set_data(self, std, mean):
        self.std = std
        self.mean = mean
        