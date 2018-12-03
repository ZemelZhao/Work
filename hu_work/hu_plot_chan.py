import matplotlib.pyplot as plt

import numpy as np

data = np.load('feat_td3.npy')
print(data)
a = 0
b = 1

max_num_x = max(max(data[:, a]),
              max(data[:, a+4]),
              max(data[:, a+8]),
              max(data[:, a+12]))
max_num_y = max(max(data[:, b]),
                max(data[:, b+4]),
                max(data[:, b+8]),
                max(data[:, b+12]))
plt.scatter(data[:, a]/max_num_x, data[:, b]/max_num_y, c='', marker='o', edgecolor='g', label='   ')
plt.scatter(data[:, a+4]/max_num_x, data[:, b+4]/max_num_y, c='', marker='o', edgecolor='r', label='   ')
plt.scatter(data[:, a+8]/max_num_x, data[:, b+8]/max_num_y, c='', marker='o',edgecolor='darkviolet', label='  ')
plt.scatter(data[:, a+12]/max_num_x, data[:, b+12]/max_num_y, c='', marker='o', edgecolor='b', label='   ')

plt.legend(loc='upper right')
plt.show()
