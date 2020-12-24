# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 15:17:25 2020

@author: Hp
"""

import pandas as pd, numpy as np
import os, matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.api as sm
import pmdarima as pm
from statsmodels.tsa.statespace.sarimax import SARIMAX



# change working directory to script path

os.chdir('C:/Users/Hp/Desktop/progettoSupp/ilMioProgetto/SsdWebApi')

df = pd.read_csv('FTSE_MIB.csv',usecols=['FTSE_MIB'], header=0) # dataframe (series)
plt.title('FTSE_MIB', color='black')
df.plot(y='FTSE_MIB')
plt.show()
ds = df.FTSE_MIB

aSales = df['FTSE_MIB'].to_numpy() # array of sales data
logdata = np.log(aSales) # log transform
data = pd.Series(logdata) # convert to pandas series



cutpoint = int(0.9*len(data))
train = data[:cutpoint]
test = data[cutpoint:]

plt.rcParams['figure.figsize'] = (10.0, 6.0)
result = seasonal_decompose(train, model='additive',freq=365)
result.plot()
plt.show()

#Sarimax model  
from statsmodels.tsa.statespace.sarimax import SARIMAX
sarima_model = SARIMAX(train, order=(1,1,0), seasonal_order=(0,1,1,5))
sfit = sarima_model.fit(maxiter=200, method='nm')
sarima_model.summary()
sfit.plot_diagnostics(figsize=(10, 6))
plt.show()

#dati di predicton non di forcast ancora detto prediction in sample

ypred=sfit.predict(start=0,end=len(train))
forewrap = sfit.get_forecast(steps=523)
forecast_ci = forewrap.conf_int()
forecast_val = forewrap.predicted_mean
plt.plot(data)
plt.plot(ypred)
plt.plot(forecast_val)
plt.title("trian")

def forecast_accuracy(forecast_val, test):

    rmse = np.mean((forecast_val - test)**2)**.523 # RMSE
    return({ 'rmse':rmse})
print( forecast_accuracy(forecast_val, test) )

yplog = pd.Series(ypred)
expdata = np.exp(yplog) # unlog
expfore = np.exp(forecast_val)
plt.plot([None for x in ypred]+[x for x in expdata[4700:]])
plt.plot(data)
plt.plot([None for x in expdata]+[x for x in expfore])
plt.show




"""

sarima_model = SARIMAX(train, order=(1,0,0), seasonal_order=(0,1,1,5))
sfit = sarima_model.fit(train)
sfit.plot_diagnostics(figsize=(10, 6))
plt.show()




ypred = sfit.predict(start=0,end=len(train)
yfore = sfit.predict(n_periods=523) # forecast
plt.plot(df.FTSE_MIB)
plt.plot(ypred)
plt.xlabel('time');plt.ylabel('sales')
plt.show()
"""
"""fitted = model.fit(train)
ypred = fitted.predict_in_sample()
yfore = fitted.predict(n_periods=523) # forecast
plt.plot(data)
plt.plot(ypred)
plt.plot([None for i in ypred]+ [x for x in yfore])
plt.xlabel('months');plt.ylabel('FTSE_MIB')
plt.show()"""




        