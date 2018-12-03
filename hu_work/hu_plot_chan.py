import matplotlib.pyplot as plt

import numpy as np

data = np.load('feat_ar.npy')
print(data)
a = 1
b = 7

max_num_x = max(max(np.abs(data[:, a])),
              max(np.abs(data[:, a+24])),
              max(np.abs(data[:, a+48])),
              max(np.abs(data[:, a+72])))
max_num_y = max(max(np.abs(data[:, b])),
                max(np.abs(data[:, b+24])),
                max(np.abs(data[:, b+48])),
                max(np.abs(data[:, b+72])))
plt.scatter(data[:, a]/max_num_x, data[:, b]/max_num_y, c='', marker='o', edgecolor='g', label='   ')
plt.scatter(data[:, a+24]/max_num_x, data[:, b+24]/max_num_y, c='', marker='o', edgecolor='r', label='   ')
plt.scatter(data[:, a+48]/max_num_x, data[:, b+48]/max_num_y, c='', marker='o',edgecolor='darkviolet', label='  ')
plt.scatter(data[:, a+72]/max_num_x, data[:, b+72]/max_num_y, c='', marker='o', edgecolor='b', label='   ')

plt.legend(loc='upper right')
plt.show()
