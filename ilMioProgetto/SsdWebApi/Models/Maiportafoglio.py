import os, sys, io, base64
import pandas as pd, matplotlib.pyplot as plt , numpy as np
from statsmodels.tsa.arima_model import ARIMA
import pmdarima as pm
from statsmodels.tsa.seasonal import seasonal_decompose
import PSO as ParSwarm
import matplotlib.pyplot as plt
from ForcastSerie import forcastValues


abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
     
capital_value = 100000
numvar = 7
xmin = 0.05
xmax = 0.80
niter = 150
popsize = 80
nhood_size = 10
horizon_data_length=523
    #optimizzation 
PSO = ParSwarm.ParSwarmOpt(xmin, xmax)
res = PSO.pso_solve(popsize, numvar, niter, nhood_size, capital_value, horizon_data_length, forcastValues)
    
#print asset values
print("Portafolio: ", end='')
print(res.xsolbest, end='')
           
print("portafoglio Return is: {}".format(res.return_valuebest))
print("portafoglio risk is: {}".format(res.devstbest))
    
    
    
    #prova generate portfoglio
    