import matplotlib.pyplot as plt
import numpy as np

arr0 = np.array([0])
arr0 = np.tile(arr0, 20)
arr1 = np.array([1])
arr1 = np.tile(arr1, 20)
arr = np.append(arr0, arr1)
print(arr)
label = ["0"]
label = label + ["%d$\pi$" % i for i in range(1, 5)]
print(label)

real = np.arange(0, 2.05, .01)
imag = np.sqrt(2**2 - real*real)

plt.plot(real, imag)
plt.grid(True)

ticks = np.arange(0, 2.01, .05)
plt.xticks(ticks)
plt.yticks(ticks)

plt.show()
