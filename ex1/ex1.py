# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 16:37:39 2019

@author: FQ538HD
"""

from utils import StatsData

female_data = StatsData()
female_data.set_data(std=2.7, mean=63.7)
print('{}: {:1.2f} in'.format('Female lowest 2.2% height', female_data.get_value_by_z(percentage=0.978)))
female_data.plot_random_sample(size=1000, label='Female distribution', color='pink')

male_data = StatsData()
male_data.set_data(std=2.9, mean=69.1)
print('{}: {:1.2f} in'.format('Male lowest 2.2% height', male_data.get_value_by_z(percentage=0.978)))
male_data.plot_random_sample(size=1000, label='Male distribution', color='skyblue')
