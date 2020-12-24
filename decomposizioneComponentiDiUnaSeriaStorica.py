# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 19:55:33 2020

@author: Hp
"""

import os
import pandas as pd
from matplotlib import pyplot as plot
from statsmodels.tsa.seasonal import seasonal_decompose

os.chdir('C:/Users/Hp/Desktop/progettoSupp/ilMioProgetto/SsdWebApi')
series = pd.read_csv('MSCI_EM.csv',usecols=[0], header=0)

""" splittare dati della serie """
X = series.values
train_size = int(len(X) * 0.90)
train, test = X[0:train_size], X[train_size:len(X)]
print('Observations: %d' % (len(X)))
print('Training Observations: %d' % (len(train)))
print('Testing Observations: %d' % (len(test)))

""" decomposizione """

plot.rcParams['figure.figsize'] = (10.0, 6.0)
result = seasonal_decompose(train, model='multiplicative',freq=86)
result.plot()
plot.show()