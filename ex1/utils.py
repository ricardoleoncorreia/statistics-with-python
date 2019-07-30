# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 16:33:08 2019

@author: Ricardo Leon
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

class StatsData:
    
    def __init__(self):
        self.std = 0
        self.mean = 0
    
    def plot_random_sample(self, size=1000, label=None, decimals=1, color='Orange'):
        normal_dist_samples = np.random.normal(loc=self.mean, scale=self.std, size=size)
        new_samples = np.round(normal_dist_samples, decimals)
        plt.hist(new_samples, label=label, color=color)
        
    def get_value_by_z(self, percentage):
        z = st.norm.ppf(percentage)
        return self.mean + self.std * z
    
    def set_data(self, std, mean):
        self.std = std
        self.mean = mean
        