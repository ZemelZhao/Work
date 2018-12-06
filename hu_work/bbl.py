import csv
import numpy as np
import matplotlib.pyplot as plt

with open('bbl.csv', 'r') as f:
    reader = csv.reader(f)
    rows = [row for row in reader]

for i in range(len(rows)):
    temp = [int(i) for i in rows[i][0].split(':')]
    temp = 3600*temp[0] + 60*temp[1] + temp[2] + temp[3] / 1000
    rows[i][0] = temp
    for j in range(1, len(rows[0])):
        rows[i][j] = float(rows[i][j])

temp = rows[0][0]
start = 400
end = 800
for i in range(len(rows)):
    rows[i][0] -= temp

rows = np.array(rows)
x_change = 0.2
y_change = -0.05
z_change = -0.6
x_multi = 1
y_multi = 5
z_multi = 3


plt.plot(rows[:end-start, 0], x_multi*(rows[start:end, 1] + x_change), label='                          ')
plt.plot(rows[:end-start, 0], y_multi*(rows[start:end, 2] + y_change), label='                          ', linestyle='--')
plt.plot(rows[:end-start, 0], z_multi*(rows[start:end, 3] + z_change), label='                          ', linestyle='-.')

plt.plot(rows[:end-start, 0], x_multi*(rows[start:end, 4] + x_change), label='                      ')
plt.plot(rows[:end-start, 0], y_multi*(rows[start:end, 5] + y_change), label='                      ', linestyle='--')
plt.plot(rows[:end-start, 0], z_multi*(rows[start:end, 6] + z_change), label='                      ', linestyle='-.')
plt.ylabel('      ')
plt.xlabel('     ')
plt.ylim(-0.4, 1.2)
plt.legend(loc='upper right')

min_num = float('inf')
for _ in range(3):
    res = []
    for i in range(1, 1000):
        temp = np.mean(np.fabs(rows[i:, _+1] - rows[:-i, _+4]))
        if temp < min_num:
            min_num = temp
            res.append(i)
    print(res[-1]/10)
    res = np.mean(np.fabs(rows[:, _+1] - rows[:, _+4]))
    print(res)
plt.show()


