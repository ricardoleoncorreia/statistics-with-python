# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 19:13:14 2019

@author: FQ538HD
"""

from utils import WallStreetData

mean = 95.70 # USD
std = 1247 # USD
n = 100 # trades
profit = 20000 # USD

data = WallStreetData()
data.set_data(std=std, mean=mean)

print('The probability to make a loss in a week: {:.2f}%'.format(data.get_probability_of_profit_in_week(profit=0, n=n)))
print('The probability to make over $20.000 in a week: {:.2f}%'.format(100-data.get_probability_of_profit_in_week(profit=profit, n=n)))
