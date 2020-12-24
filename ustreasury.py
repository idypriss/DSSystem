# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 10:24:14 2020

@author: Hp
"""

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
df = pd.read_csv('US_Treasury.csv', header=0,usecols=['US_Treasury'])
ds= df.US_Treasury
df.plot(y='US_Treasury')
plt._show()

npa = df['US_Treasury'].to_numpy()
logdata = np.log(npa)
data = pd.Series(logdata).diff()



cutpoint = int(0.9*len(data))
train = data[:cutpoint]
test = data[cutpoint:]
train[0]=0


arima = sm.tsa.statespace.SARIMAX(train,order=(2,0,1),seasonal_order=(0,0,0,0)).fit()
arima.summary()

from sklearn.metrics import mean_squared_error
pred =arima.predict(4700,5223)[1:]
print('ARIMA model MSE:{}'.format(mean_squared_error(test,pred)))

pd.DataFrame({'test':test,'pred':pred}).plot();plt.show()


model = pm.auto_arima(train, start_p=1, start_q=1,
                        test='adf', max_p=6, max_q=6,
                        start_P=0, seasonal=False,
                        d=None, D=None, trace=True,
                        error_action='ignore',
                        suppress_warnings=True,
                        stepwise=False,approximation=False) # False full grid
print(model.summary())
morder = model.order; print("Sarimax order {0}".format(morder))
mseasorder = model.seasonal_order;
print("Sarimax seasonal order {0}".format(mseasorder))



resDiff = sm.tsa.arma_order_select_ic(train, max_ar=7, max_ma=7, ic='aic', trend='nc')
print('ARMA(p,q) =',resDiff['aic_min_order'],'is the best.')

npa = df['US_Treasury'].to_numpy()
logdata = np.log(npa)
plt.plot(npa, color = 'blue', marker = "o")
plt.plot(logdata, color = 'red', marker = "o")
plt.title("numpy.log()")
plt.xlabel("x");plt.ylabel("logdata")
plt.show() 



plt.rcParams['figure.figsize'] = (10.0, 6.0)
result = seasonal_decompose(ds, model='multiplicative',freq=12)
result.plot()
plt.show()

data = pd.Series(logdata).diff()
data.plot(y='GOLD_SPOT')
plt.show()

sm.graphics.tsa.plot_acf(data.diff().dropna(), lags=500)
plt.show()
sm.graphics.tsa.plot_pacf(data.diff().dropna(), lags=500)
plt.show()

cutpoint = int(0.9*len(data))
train = data[:cutpoint]
test = data[cutpoint:]

train[0]=0

sarima_model = SARIMAX(train, order=(6,0,5), seasonal_order=(0,0,0,0))
sfit = sarima_model.fit(train)
sfit.plot_diagnostics(figsize=(10, 6))
plt.show()
print(sfit.summary())


"""diffdata = data.diff()
diffdata[0] = df['US_Treasury'][0] # reset 1st ele

sm.graphics.tsa.plot_acf(data.values, lags=245)
plt.show()
#sm.graphics.tsa.plot_pacf(data.values, lags=5000)
plt.show()"""



# splitting of data 70-30

cutpoint = int(0.9*len(data))
train = data[:cutpoint]
test = data[cutpoint:]





# auto arimag
model = pm.auto_arima(train.values, start_p=1, start_q=1,
                        test='adf', max_p=6, max_q=6, m=1,
                        start_P=0, seasonal=False,
                        d=None, D=None, trace=True,
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
plt.show() 





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


