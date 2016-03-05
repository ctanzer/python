import matplotlib.pyplot as plt
import numpy as np

f_rx = np.arange(935, 960.01, .01)
f_tx = f_rx - 45
f_lo = f_rx + 203
f_zf = f_lo - f_rx

fig = plt.figure()

plt.plot(f_rx, f_rx, 'g', label='f_rx')
plt.plot(f_rx, f_tx, 'g', label='f_tx')
plt.plot(f_rx, f_lo, 'b', label='f_lo')
for i in np.arange(1, 21):
    for j in np.arange(1, 3):
        if j == i:
            continue
        plt.plot(f_rx, np.abs(j*f_lo - i*f_zf), 'r', label='{j}*f_lo-{i}*f_zf'.format(j=j, i=i))

plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)
# fig.tight_layout()

plt.show()
