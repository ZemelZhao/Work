# -*- coding: utf-8 -*-
import pandas as pd
import scipy.io as scio
import numpy as np
import os
import time
import random
import tensorflow as tf

def LoadCsvData(dataPath,DataColumnsNames=[],isLaptop=False,chunkSize=None):
    if 'http' in dataPath:
        dataPath = tf.keras.utils.get_file(dataPath.split('/')[-1],dataPath)
    try:
        rawData = pd.read_csv(dataPath,names=DataColumnsNames,header=0,chunksize=chunkSize if isLaptop else None)
        return rawData
    except:
        return None

def feat_extra(data,useAR = True):
    def feat_TD(data):
        data = np.array(data)
        data_result = []
        data_result.append(np.sum(np.abs(data)))
        data_result.append(np.sum(np.abs(data[1:]-data[:-1])))
        data_result.append(np.sum(data[1:]*data[:-1]<0))
        data_result.append(np.sum((data[:-2]-data[1:-1])*(data[1:-1]-data[2:])>=0))
        return data_result

    def feat_ARBurg(data):
        ret = 8*[0.0]
        res = ret[:]
        ret[0] = 1.0
        res[0] = 1.0
        matall = np.vstack((np.array(data),np.array(data)))
        for i in range(1,8):
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

    allChannels = np.array(data.copy()).T
    fea = []
    for channel in allChannels:
        fea += feat_TD(channel)
        if useAR:
            fea += feat_ARBurg(channel)
    return fea

def PreProcessDataMap(rawData,featExtraFunc,winLength,winIncrement):
    start = time.clock()
    features = []
    labels = []

    index = 0
    while index+winLength < len(rawData):
        if rawData.iloc[index,-1] != rawData.iloc[index+winLength,-1]:
            index += winLength
        else:
            oneFeature = featExtraFunc(rawData.iloc[index:index+winLength,0:-1])
            features.append(oneFeature)
            labels.append(rawData.iloc[int(index+winLength/2),-1])
            index += winIncrement

    elapsed = (time.clock() - start)
    print("Time used:",elapsed)
    return features,labels

def load_data(fealabelDict,trainDataFactor,uniSampling=True):
    train_x = []
    train_y = []
    test_x = []
    test_y = []
    if uniSampling:
        sampleNum = min([len(value) for value in fealabelDict.values()])
        trainNum = int(sampleNum*trainDataFactor)
        for label,feature in fealabelDict.items():
            random.shuffle(feature)
            train_x.extend(feature[:trainNum])
            train_y.extend([label]*trainNum)
            test_x.extend(feature[trainNum:sampleNum])
            test_y.extend([label]*(sampleNum-trainNum))
    else:
        for label,feature in fealabelDict.items():
            random.shuffle(feature)
            trainNum = int(len(feature)*trainDataFactor)
            train_x.extend(feature[:trainNum])
            train_y.extend([label]*trainNum)
            test_x.extend(feature[trainNum:])
            test_y.extend([label]*len(feature[trainNum:]))
    return (train_x,train_y),(test_x,test_y)

if __name__ == '__main__':
    print("Test speed of server")
    dataPath = r'S2.csv'
    dataUrl = r'http://bbl.sjturover.com:8080/download/Ninapro/Data2/csvFile/S2.csv'
    dataColumnsNames = ['emg0','emg1','emg2','emg3','emg4','emg5','emg6','emg7','emg8','emg9','emg10','emg11','label']
    rawData = LoadCsvData(dataPath,dataColumnsNames)
    print(type(rawData)) #<class 'pandas.core.frame.DataFrame'>

    features,labels = PreProcessDataMap(rawData,feat_extra,300,100)
    fealabelMapDict = {i:[] for i in range(18)}
    for i in range(len(features)):
        fealabelMapDict[labels[i]].append(features[i])
    for label,feature in fealabelMapDict.items():
        print("label: {0}, fetureNum: {1}".format(label,len(feature)))

    (train_x,train_y),(test_x,test_y) = load_data(fealabelMapDict,0.7,True)
    print("train_x len: {0}\ntrain_y len: {1}\ntest_x len: {2}\ntrain_x len: {3}\n".format(len(train_x),len(train_y),len(test_x),len(test_y)))


