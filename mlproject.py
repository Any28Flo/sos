# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 20:30:50 2018

@author: analin
"""


import pandas as pd
#save filepath to variable for easier access
data_path = 'dataset/IDVFC_NM.csv'
data = pd.read_csv(data_path, encoding = 'utf-8')
print data.head()

print data.describe()