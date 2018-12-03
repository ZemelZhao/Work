import numpy as np
import csv
import os

def feat_ARBurg(data):
    ret = 5*[0.0]
    res = ret[:]
    ret[0] = 1.0
    res[0] = 1.0
    matall = np.vstack((np.array(data),np.array(data)))
    for i in range(1,5):
        sumn = 0.0
        sumd = 0.0
        mat = matall[:,i-1:]
        matold = mat.copy()

        sumn = mat[0,1:].dot(mat[1,:-1].T)
        sumd = mat[0,1:].dot(mat[0,1:].T)+mat[1,:-1].dot(mat[1,:-1].T)
        garma = -2*sumn/sumd

        for j in range(1,i+1):
            res[j] = ret[j]+garma*ret[i-j]
        ret = res[:]
        mat[1,1:] = mat[1,:-1] + garma*mat[0,1:]
        mat[0,1:] = mat[0,1:] + garma*matold[1,:-1]
        matall[:,i-1:] = mat
    return res[1:]

for _ in [0, 1, 3, 4]:
    data_file = os.path.join('emgdata', '%i.csv' %_)
    for i in range(0, 8, 2):
        data_cache = []
        reader = csv.reader(open(data_file))
        for row in reader:
            data_cache.append(float(row[i]))
        data_cache = data_cache[1000 : -1000]
        feat_td_temp = np.array(4*[0])
        for j in range(0, 2900, 100):
            data_temp = data_cache[j : j + 100]
            feat_td_temp = np.vstack((feat_td_temp, feat_ARBurg(data_temp)))
        try:
            feat_td = np.hstack((feat_td, feat_td_temp))
        except NameError:
            feat_td = feat_td_temp

np.save('feat_ar.npy', feat_td)
print(feat_td.shape)
