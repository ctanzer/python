import csv
import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt('../../Temp_Files/test.csv', delimiter=' ', names=['x','y'])
data2 = np.loadtxt('../../Temp_Files/test.csv',delimiter=' ')

# print (data['x'])


# fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
# ax1.plot(data['x'], data['y'], color='r')
# ax1.grid(True)
# ax2.plot(data2[:,0], data2[:,2], color='g')
# ax2.grid(True)

## Two subplots, unpack the output array immediately
# f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
# ax1.plot(data['x'], data['y'], color='r')
# ax1.set_title('Sharing Y axis')
# ax2.scatter(data2[:,0], data2[:,1])

# plt.plot(data['x'], data['y'], color='r')
plt.plot(data['x'], data['y'], 'r', data2[:,0], data2[:,1]/2, 'g')
plt.grid(True)
# plt.plot(data2[:,0], data2[:,1], color='g')
plt.show()
