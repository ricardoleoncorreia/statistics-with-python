# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 19:31:20 2019

@author: FQ538HD
"""

from utils import TvData

mean = 26.5 # hours of TV a week
std = 10 # hrs
n = 50 # millenials
new_mean = 24 # hours of TV per week
alfa = 5 # required % of confidence

data = TvData()
data.set_data(mean=mean, std=std)
print(data.hypothesis_testing_result(new_mean=new_mean, n=n, alfa=alfa))
