# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 15:08:58 2020

@author: Hp
"""

import pandas as pd, numpy as np, os
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf
from statsmodels.tsa.stattools import pacf
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
import pmdarima as pm
from statsmodels.tsa.statespace.sarimax import SARIMAX



os.chdir('C:/Users/Hp/Desktop/progettoSupp/ilMioProgetto/SsdWebApi')
df = pd.read_csv('GOLD_SPOT.csv', header=0,usecols=['GOLD_SPOT'])
ds= df.All_Bonds
df.plot(y='GOLD_SPOT')
plt._show()


npa = df['GOLD_SPOT'].to_numpy()
logdata = np.log(npa)
data = pd.Series(logdata).diff()
data.plot(y='GOLD_SPOT')
plt.show()

cutpoint = int(0.9*len(data))
train = data[:cutpoint]
test = data[cutpoint:]

train[0]=0

model = SARIMAX(train, order=(2,0,2), seasonal_order=(0,0,0,0))
sfit = model.fit(train)
print(sfit.summary())

sfit = model.fit(train)
sfit.plot_diagnostics(figsize=(10, 6))
plt.show()
print(sfit.summary())

ypred = sfit.predict_in_sample() # prediction (in-sample)
yfore = sfit.predict(n_periods=480)

plt.plot(data)
plt.plot(ypred)
plt.plot([None for i in ypred] + [x for x in yfore])
plt.xlabel('time');plt.ylabel('log_GOLD_SPOT')
plt.show() 









