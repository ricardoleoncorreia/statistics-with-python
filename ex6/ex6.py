# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 11:23:33 2019

@author: FQ538HD
"""

old_p = 23 # % which were leading to high return rates from clients.
significance = 95 # %
desired_p = 18 # %
n = 150 # spoons
spoon_defects = 23 # % spoons have defects.

from utils import SpoonsData

new_p = 100 * spoon_defects / n

data = SpoonsData()
data.set_data(p=desired_p)
data.proportion_testing_result(n=n, new_mean=new_p, significance=significance)
