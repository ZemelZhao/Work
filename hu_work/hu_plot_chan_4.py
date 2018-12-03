import matplotlib.pyplot as plt

import numpy as np

data = np.load('feat_ar.npy')
print(data)
z = 3
a = z
c = 4
b = z + c

max_num_x = max(max(np.abs(data[:, a])),
              max(np.abs(data[:, a+4*c])),
              max(np.abs(data[:, a+8*c])),
              max(np.abs(data[:, a+12*c])))
max_num_y = max(max(np.abs(data[:, b])),
                max(np.abs(data[:, b+4*c])),
                max(np.abs(data[:, b+8*c])),
                max(np.abs(data[:, b+12*c])))
plt.scatter(data[:, a]/max_num_x, data[:, b]/max_num_y, c='', marker='o', edgecolor='g', label='   ')
plt.scatter(data[:, a+4*c]/max_num_x, data[:, b+4*c]/max_num_y, c='', marker='o', edgecolor='r', label='   ')
plt.scatter(data[:, a+8*c]/max_num_x, data[:, b+8*c]/max_num_y, c='', marker='o',edgecolor='darkviolet', label='  ')
plt.scatter(data[:, a+12*c]/max_num_x, data[:, b+12*c]/max_num_y, c='', marker='o', edgecolor='b', label='   ')

plt.legend(loc='upper right')
plt.show()
