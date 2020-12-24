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
import warnings
from statsmodels.tools.sm_exceptions import ConvergenceWarning





# change working directory to script path

os.chdir('C:/Users/Hp/Desktop/progettoSupp/ilMioProgetto/SsdWebApi')

df = pd.read_csv('FTSE_MIB.csv',usecols=['FTSE_MIB'], header=0) # dataframe (series)
plt.title('FTSE_MIB', color='black')
df.plot(y='FTSE_MIB')
plt.show()
ds = df.FTSE_MIB

aSales = df['FTSE_MIB'].to_numpy() # array of sales data
logdata = np.log(aSales) # log transform
data = pd.Series(logdata)# convert to pandas series
data.plot()
plt.show()


cutpoint = int(0.9*len(ds))
train =ds[:cutpoint]
test = ds[cutpoint:]

train[0] = 0 

#reconstruct = np.exp(np.r_[train,test].cumsum()+logdata[0])

#Sarimax model  
sarima_model = SARIMAX(train, order=(1,0,1), seasonal_order=(0,0,0,0))
sfit = sarima_model.fit(train)
sfit.plot_diagnostics(figsize=(10, 6))
plt.show()
print(sfit.summary())


#dati di predicton non di forcast ancora detto prediction in sample
ypred=sfit.predict(start=0,end=len(train))
#forewrap = sfit.get_forecast(steps=523)
#forecast_ci = forewrap.conf_int()
#forecast_val = forewrap.predicted_mean
plt.plot(train)
plt.plot(ypred, color='green')
#plt.plot(forecast_val)
plt.title("trian")

"""def forecast_accuracy(forecast_val, test):

    rmse = np.mean((forecast_val - test)**2)**.523 # RMSE
    return({ 'rmse':rmse})
print( forecast_accuracy(forecast_val, test) )"""




        