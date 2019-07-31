# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 11:23:20 2019

@author: FQ538HD
"""

import numpy as np
import scipy.stats as st

class SpoonsData:
    
    def __init__(self):
        self.p = 0
        self.q = 0
    
    def alert_message(self):
        print('Conditions to use Proportion Testing were not satisfied')
        
    def are_conditions_valid(self, n):
        return n * self.p > 10 and n * self.q > 10
    
    def proportion_testing_result(self, n, new_mean, significance):
        if self.are_conditions_valid(n=n):
            mean = self.p
            std = np.sqrt(self.p * self.q)
            s = std / np.sqrt(n) # Central limit theorem
            z = ((new_mean / 100) - mean) / s
            probability = 100 * st.norm.cdf(z)
            val_str = 'not' if probability > 1 - significance else ''
            print('Null hypothesis can{} be rejected ({:0.2f}% confidence)'.format(val_str, 100 - probability))
        else:
            self.alert_message()
        
    def set_data(self, p):
        self.p = p / 100
        self.q = 1 - self.p
