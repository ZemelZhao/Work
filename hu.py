import numpy as np
import csv
import pandas as pd
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot
import os


def td(data):
    data = np.array(data)
    cache = []
    cache.append(np.mean(np.fabs(data)))
    cache.append(np.var(data))
    cache.append(np.sum(data[1:]*data[:-1] < 0))
    cache.append(np.sum((data[:-2] - data[1:-1])*(data[1:-1] - data[2:])>=0))
    return np.array(cache)

for _ in [0, 1, 3, 4]:

    data_file = os.path.join('emgdata', '%i.csv' %_)

    for i in range(0, 7, 2):
        data_cache = []
        reader = csv.reader(open(data_file))
        for row in reader:
            data_cache.append(float(row[i]))
        data_cache = data_cache[1000: -1000]
        feat_td_temp = np.array([0, 0, 0, 0])
        for j in range(0, 2900, 100):
            data_temp = data_cache[j : j + 100]
            feat_td_temp = np.vstack((feat_td_temp, td(data_temp)))
        try:
            feat_td = np.hstack((feat_td, feat_td_temp))
        except:
            feat_td = feat_td_temp

    np.save('feat_td%i.npy' % _, feat_td)

