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
ds= df.GOLD_SPOT
df.plot(y='GOLD_SPOT')
plt._show()

plt.rcParams['figure.figsize'] = (10.0, 6.0)
result = seasonal_decompose(ds, model='additive',freq=262)
result.plot()
plt.show()


npa = df['GOLD_SPOT'].to_numpy()
logdata = np.log(npa)
plt.plot(npa, color = 'blue', marker = "o")
plt.plot(logdata, color = 'red', marker = "o")
plt.title("numpy.log()")
plt.xlabel("x");plt.ylabel("logdata")
plt.show() 

data = pd.Series(logdata).diff()
data.plot(y='GOLD_SPOT')
plt.show()
cutpoint = int(0.9*len(ds))
train = ds[:cutpoint]
test = ds[cutpoint:]

train[0]=0
arima = sm.tsa.statespace.SARIMAX(train,order=(1,0,0),seasonal_order=(0,0,0,0),
                                 enforce_stationarity=False, enforce_invertibility=False,).fit()
arima.summary()

res = arima.resid
fig,ax = plt.subplots(2,1,figsize=(15,8))
fig = sm.graphics.tsa.plot_acf(res, lags=50, ax=ax[0])
fig = sm.graphics.tsa.plot_pacf(res, lags=50, ax=ax[1])
plt.show()


from sklearn.metrics import mean_squared_error
pred = arima.predict(4700,5223)[1:]
print('ARIMA model MSE:{}'.format(mean_squared_error(test,pred)))

pd.DataFrame({'test':test,'pred':pred}).plot();plt.show()
#forecast and prevision

fitted = arima.fit(train)
ypred = fitted.predict_in_sample() # prediction (in-sample)
yfore = fitted.predict(n_periods=480) # forecast (out-of-sample)

plt.plot(train.values)
plt.plot(ypred)
plt.plot([None for i in ypred] + [x for x in yfore])
plt.xlabel('time');plt.ylabel('log_US_Treasury')
plt.show() """


sm.graphics.tsa.plot_acf(data.diff().dropna(), lags=500)
plt.show()
sm.graphics.tsa.plot_pacf(data.diff().dropna(), lags=500)
plt.show()





plt.plot(data[0:86].dropna().values)
#plt.plot(data[87:522].dropna().values)
plt.plot(data[523:782].dropna().values);plt.show()
#plt.plot(data[785:1046].dropna().values)
#plt.plot(data[1046:1305].dropna().values);plt.show()





"""diffdata = data.diff()
diffdata[0] = df['US_Treasury'][0] # reset 1st ele

sm.graphics.tsa.plot_acf(data.values, lags=245)
plt.show()
#sm.graphics.tsa.plot_pacf(data.values, lags=5000)
plt.show()"""

"""

# splitting of data 70-30

cutpoint = int(0.9*len(data))
train = data[:cutpoint]
test = data[cutpoint:]





# auto arimag
model = pm.auto_arima(train.values, start_p=1, start_q=1,
                        test='adf', max_p=4, max_q=4, m=1,
                        start_P=0, seasonal=True,
                        d=None, D=1, trace=True,
                        error_action='ignore',
                        suppress_warnings=True,
                        stepwise=True) # False full grid
print(model.summary())
morder = model.order; print("Sarimax order {0}".format(morder))
mseasorder = model.seasonal_order;
print("Sarimax seasonal order {0}".format(mseasorder))

#forecast and prevision

fitted = model.fit(train)
ypred = fitted.predict_in_sample() # prediction (in-sample)
yfore = fitted.predict(n_periods=280) # forecast (out-of-sample)

plt.plot(train.values)
plt.plot(ypred)
plt.plot([None for i in ypred] + [x for x in yfore])
plt.xlabel('time');plt.ylabel('log_US_Treasury')
plt.show() """





"""import os, numpy as np, pandas as pd, matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf
# Import data

# Accuracy metrics
def forecast_accuracy(yfore, test):

    rmse = np.mean((yfore - test)**2)**.523 # RMSE
    acf1 = acf(yfore-test)[1] # ACF1
    ds= rmse
    nrmse = ds.to_numpy()
    rms = np.sqrt(nrmse)
    return({ 'rmse':rms, 'acf1':acf1,})
print( forecast_accuracy(yfore, test) )"""
    
"""corr = np.corrcoef(forecast, actual)[0,1] # corr
mins = np.amin(np.hstack([forecast[:,None], actual[:,None]]), axis=1)
maxs = np.amax(np.hstack([forecast[:,None], actual[:,None]]), axis=1)
minmax = 1 - np.mean(mins/maxs) # minmax"""


