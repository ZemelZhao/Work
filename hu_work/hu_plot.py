import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
feat_td0 = np.load('feat_td0.npy')
feat_td1 = np.load('feat_td1.npy')
feat_td3 = np.load('feat_td3.npy')
feat_td4 = np.load('feat_td4.npy')

feat_td = np.vstack((feat_td0, feat_td1, feat_td3, feat_td4))

pca = PCA(n_components=2)
data = pca.fit_transform(feat_td)
plt.scatter(data[:30, 0], np.array(30*[0]), c='r')
plt.scatter(data[30:60, 0], np.array(30*[0]), c='b')
plt.scatter(data[60:90, 0], np.array(30*[0]), c='g')
plt.scatter(data[90:120, 0], np.array(30*[0]), c='purple')
plt.show()
