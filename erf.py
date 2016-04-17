import math
import numpy as np
import scipy.special as sci
import matplotlib.pyplot as plt

def getErf(x):
    return math.erf(x)

x = np.linspace(-3, 3, num=100)
y = sci.erf(x)

plt.plot(x, y)
plt.grid(True)
plt.show()
