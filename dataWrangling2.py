#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 06:34:14 2019

@author: analin
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
mainpath = "/home/analin/Documents/tesisDataMining/sosProject/dataset"
filename = "IDVFC_NM_1.csv"
fullpath = os.path.join(mainpath, filename)
data = pd.read_csv(fullpath)
data.head()
data.columns.values
data.shape
data.describe()
