
import numpy as np
import pandas as pd
from scipy import stats # to be used later
import matplotlib.pyplot as plt
import os

os.chdir('C:/Users/Hp/Downloads')
df = pd.read_csv('dati1.csv') 

#df = pd.read_csv('C:/Users/Hp/Downloads/dati1.csv') # dataframe (series)
npa = df[';'].to_numpy()  # numpy array
#npa2 = df['serie2'].to_numpy() # numpy array




