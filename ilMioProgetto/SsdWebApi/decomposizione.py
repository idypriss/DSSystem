# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 14:50:52 2020

@author: Hp
"""

import os
import pandas as pd
from matplotlib import pyplot as plot
from statsmodels.tsa.seasonal import seasonal_decompose

os.chdir('C:/Users/Hp/Desktop/progettoSupp/ilMioProgetto/SsdWebApi')
plot.rcParams['figure.figsize'] = (10.0, 6.0)
series = pd.read_csv('C:/Users/Hp/Desktop/progettoSupp/ilMioProgetto/SsdWebApi/GOLD_SPOT.CSV',usecols=[0], header=0)
result = seasonal_decompose(series, model='multiplicative',freq=12)
result.plot()
plot.show()
