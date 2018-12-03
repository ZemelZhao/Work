import numpy as np
import csv
import os

def td(data, a):
    data = np.array(data)
    cache = []
    if a == 0:
        cache.append(np.mean(np.fabs(data)))
    elif a == 1:
        cache.append(np.mean(np.fabs(data[1:] - data[:-1])))
    elif a == 2:
        cache.append(np.sum(data[1:]*data[:-1] < 0))
    else:
        cache.append(np.sum((data[:-2] - data[1:-1])*(data[1:-1] - data[2:])>=0))
    return np.array(cache)

feat = 1

for _ in [0, 1, 3, 4]:
    data_file = os.path.join('emgdata', '%i.csv' %_)
    for i in range(1, 8, 2):
        data_cache = []
        reader = csv.reader(open(data_file))
        for row in reader:
            data_cache.append(float(row[i]))
        data_cache = data_cache[1000 : -1000]
        feat_td_temp = np.array([0])
        for j in range(0, 2900, 100):
            data_temp = data_cache[j : j + 100]
            feat_td_temp = np.vstack((feat_td_temp, td(data_temp, feat)))
        try:
            feat_td = np.hstack((feat_td, feat_td_temp))
        except NameError:
            feat_td = feat_td_temp

np.save('feat_td%i.npy' % feat, feat_td)
