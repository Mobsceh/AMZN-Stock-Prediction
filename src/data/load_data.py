#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import pandas as pd
import numpy as np

PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                           os.pardir, os.pardir))

RAW_DATA_DIR = os.path.join(PROJECT_DIR, 'data', 'raw')
DATA_DIR = os.path.join(PROJECT_DIR, 'data', 'processed')

ORG = os.path.join(RAW_DATA_DIR, 'AMZN_2006-01-01_to_2018-01-01.csv')

def loadData(path, selected_columns=None):
    data = pd.read_csv(ORG, parse_dates = ['Date'], index_col = 'Date')
    return data

