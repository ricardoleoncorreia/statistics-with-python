# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 12:15:42 2019

@author: FQ538HD
"""

from utils import BookData

old_mean = 57 # $ on average
old_std = 20 # $
n = 80 # customers
new_mean = 62 # $
significance = 95 # % confidence

data = BookData()
data.set_data(mean=old_mean, std=old_std)
data.two_tail_testing(n=n,new_mean=new_mean, significance=significance)
