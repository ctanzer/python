import math
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.arange(0, 2*np.pi, 0.01)
inphase = np.sin(x)
quadrature = np.cos(x)
iq_sig = inphase + quadrature

fig = plt.figure()
line1, line2, line3, = plt.plot(x, inphase, 'r', x, quadrature, 'g', x, iq_sig, 'b')

# f, (ax1, ax2, ax3) = plt.subplots(1, 3, sharex=True, sharey=True)
# line1, = ax1.plot(x, inphase, 'r')
# line2, = ax2.plot(x, quadrature, 'g')
# line3, = ax3.plot(x, iq_sig, 'b')
# ax1.grid(True)
# ax2.grid(True)
# ax3.grid(True)


def animate(i, l1, l2, l3):
    inphase = np.sin(x + i/100.0)
    quadrature = np.cos(x + i/100.0)
    iq_sig = inphase + quadrature
    l1.set_ydata(inphase)  # update the data
    # l2.set_ydata(quadrature)  # update the data
    l3.set_ydata(iq_sig)  # update the data
    return l1, l2, l3


ani = animation.FuncAnimation(fig, animate, np.arange(1, 628), fargs=(line1, line2, line3),
                              interval=25, blit=True)

plt.show()

# plt.plot(x, inphase, 'r', x, quadrature, 'g', x, iq_sig, 'b')
# plt.grid(True)
