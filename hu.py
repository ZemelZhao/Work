import numpy as np
import csv
from statsmodels.tsa.arima_model import ARMA, ARIMA
import os

data_file = os.path.join('emgdata', '0.csv')

reader = csv.reader(open(data_file))
data_cache = []
for row in reader:
    data_cache.append(float(row[0]))

data_cache = data_cache[1000: -1000]

