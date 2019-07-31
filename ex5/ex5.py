# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 00:28:06 2019

@author: FQ538HD
"""

from utils import HouseholdData

significance = 97 # %
p = 58 # % of American homes have tablet devices
n = 100 # random households
new_p = 73 # % of them has tablets

data = HouseholdData()
data.set_data(p=p)
data.proportion_testing_result(n=n, new_mean=new_p, significance=significance)
data.get_significance_limit(significance=significance, n=n)
