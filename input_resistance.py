import numpy as np
import matplotlib.pyplot as plt

rin = np.arange(0, 20.5, 0.1)

v = rin/(rin+1)

plt.plot(rin, v)
plt.grid(True)
plt.yticks(np.arange(0, 1.1, 0.1))
plt.show()
