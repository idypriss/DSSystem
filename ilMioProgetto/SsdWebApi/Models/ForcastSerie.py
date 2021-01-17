import os, sys, io, base64
import pandas as pd, matplotlib.pyplot as plt , numpy as np
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.seasonal import seasonal_decompose
import PSO as ParSwarm
import pmdarima as pm 
import matplotlib.pyplot as plt
import json

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

serie = ["SP_500", "FTSE_MIB", "GOLD_SPOT", "MSCI_EM", "MSCI_EURO", "All_Bonds", "US_Treasury"]

forcastValues = []
def print_figure(fig):
	"""
	Converts a figure (as created e.g. with matplotlib or seaborn) to a png image and this 
	png subsequently to a base64-string, then prints the resulting string to the console.
	"""
	buf = io.BytesIO()
	fig.savefig(buf, format='png')
	print(base64.b64encode(buf.getbuffer()))


def forecast(id):
    
    df = pd.read_csv("../%s.csv" % id, sep=str, delimiter=',',names=['values'], header=0, error_bad_lines=False,warn_bad_lines=False,keep_default_na=True)
  
    #data preprocessing 
    dataframe = df['values'].to_numpy() # array of values data
    logdata = np.log(dataframe) # log transform

    cutpoint = int(len(df) * 0.90)
    horizon_data_length = len(df) - cutpoint
    train = logdata[:cutpoint]
    test = logdata[cutpoint:]
    test=test[0:]

    #model  
    Arima_model = pm.auto_arima(train, start_p=0, start_q=0,
                        test='adf', max_p=6, max_q=6, max_d=2, trace=True,
                        error_action='ignore', suppress_warnings=True,
                        stepwise=True) 
    # Predictions
    ypred = Arima_model.predict_in_sample(start=1, end=len(train))
    forecast_val, confint = Arima_model.predict(n_periods=horizon_data_length, return_conf_int=True)
    #valutation of result
    metrics = forecast_accuracy(forecast_val, test)
    print("Mape is "+id,metrics['mape'])
    #insert value 
    yfore = []
    for j in range(0, horizon_data_length):
        print("Actual {} {} forcast {:.2f}".format(id,j,forecast_val[j]))
        yfore.append(forecast_val[j])
    
    # Plot
    plt.clf()
    plt.plot(logdata, label='LogData')
    plt.plot(ypred, label='Predict')    
    plt.plot(label='Forcast')
    plt.plot([None for i in ypred] + [x for x in yfore], label='Forcast')
    plt.title("{}".format(id))
    plt.legend()
  
    #plt.show()
    print_figure(plt.gcf())
    
    return yfore, horizon_data_length

# Accuracy metrics
def forecast_accuracy(forecast_val, test):
    mape = np.mean(np.abs(forecast_val- test)/np.abs(test)) # MAPE
    return({'mape':mape})

#Main call   
if len(sys.argv) == 2:
    forecast(sys.argv[1])
else:
    for i in range(len(serie)):
        f, horizon_data_length = forecast(serie[i])
        forcastValues.append(f)
        

    
    
   
   