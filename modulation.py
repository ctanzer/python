import math
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.arange(-2*np.pi, 2*np.pi, 0.01)
inphase = np.sin(x)
quadrature = np.cos(x)
iq_sig = inphase + quadrature

fig1 = plt.figure(1)
line1p, line2p, line3p, = plt.plot(x, inphase, 'r', x, quadrature, 'g', x, iq_sig, 'b')
fig2 = plt.figure(2)
line1a, line2a, line3a, = plt.plot(x, inphase, 'r', x, quadrature, 'g', x, iq_sig, 'b')


def animate_phase(i, l1, l2, l3):
    inphase = np.cos(x + i*np.pi/100)
    quadrature = np.cos(x)
    iq_sig = inphase + quadrature
    l1.set_ydata(inphase)  # update the data
    # l2.set_ydata(quadrature)  # update the data
    l3.set_ydata(iq_sig)  # update the data
    return l1, l2, l3

def animate_amplitude(i, l1, l2, l3):
    if i < 2:
        inphase = (1-i)*np.sin(x)
    else:
        inphase = (i-3)*np.sin(x)
    quadrature = np.cos(x)
    iq_sig = inphase + quadrature
    l1.set_ydata(inphase)  # update the data
    # l2.set_ydata(quadrature)  # update the data
    l3.set_ydata(iq_sig)  # update the data
    return l1, l2, l3


# ani = animation.FuncAnimation(fig1, animate_phase, np.arange(0, 2*np.pi, np.pi/2), fargs=(line1, line2, line3),
#                               interval=25, blit=True)
ani1 = animation.FuncAnimation(fig1, animate_phase, np.arange(0, 200), fargs=(line1p, line2p, line3p),
                              interval=25, blit=True)

ani2 = animation.FuncAnimation(fig2, animate_amplitude, np.arange(0, 4, 0.01), fargs=(line1a, line2a, line3a),
                              interval=25, blit=True)

plt.show()

# plt.plot(x, inphase, 'r', x, quadrature, 'g', x, iq_sig, 'b')
# plt.grid(True)
