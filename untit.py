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
df = pd.read_csv('All_Bonds.csv', header=0,usecols=['All_Bonds'])
ds= df.All_Bonds
df.plot(y='All_Bonds')
plt._show()


npa = df['All_Bonds'].to_numpy()
logdata = np.log(npa)
data = pd.Series(logdata).diff()
data.plot(y='GOLD_SPOT')
plt.show()

cutpoint = int(0.9*len(data))
train = data[:cutpoint]
test = data[cutpoint:]

train[0]=0

model = pm.auto_arima(train, start_p=1, start_q=1,
                        test='adf', max_p=6, max_q=6,
                        start_P=0, seasonal=False,
                        d=None, D=None, trace=True,
                        error_action='ignore',
                        suppress_warnings=True,
                        stepwise=False,approximation=False)

 # False full grid
print(model.summary())
morder = model.order; print("Sarimax order {0}".format(morder))
mseasorder = model.seasonal_order;
print("Sarimax seasonal order {0}".format(mseasorder))


sfit = model.fit(train)
sfit.plot_diagnostics(figsize=(10, 6))
plt.show()
print(sfit.summary())

ypred = sfit.predict_in_sample() # prediction (in-sample)
yfore = sfit.predict(n_periods=480)

plt.plot(data)
plt.plot(ypred)
plt.plot([None for i in ypred] + [x for x in yfore])
plt.xlabel('time');plt.ylabel('log_US_Treasury')
plt.show() 









