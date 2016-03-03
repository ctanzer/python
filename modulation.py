import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.arange(-2*np.pi, 2*np.pi, 0.01*np.pi)
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

ani1 = animation.FuncAnimation(fig1, animate_phase, np.arange(0, 200), fargs=(line1p, line2p, line3p),
                              interval=25, blit=True)

ani2 = animation.FuncAnimation(fig2, animate_amplitude, np.arange(0, 4, 0.01), fargs=(line1a, line2a, line3a),
                              interval=25, blit=True)

x2 = np.arange(-20*np.pi, 20*np.pi, 0.01*np.pi)
arr0 = np.array([-1])
arr0 = np.tile(arr0, 1000)
arr1 = np.array([1])
arr1 = np.tile(arr1, 1000)
inphase2 = np.append(arr0, arr1)
inphase2 = np.append(inphase2, inphase2)
inphase2 = np.roll(inphase2, 250)
quadrature2 = np.roll(inphase2, 500)
carrier = np.cos(x2)
carrier90 = np.sin(x2)

fig3 = plt.figure(3)
plt.plot(x2, inphase2*carrier+quadrature2*carrier90)

ticks = np.arange(-20*np.pi, 21*np.pi, 2*np.pi)
label = ["0"]
label = ["%d$\pi$" % i for i in range(-20, 0, 2)] + label
label = label + ["%d$\pi$" % i for i in range(1, 21, 2)]
plt.xticks(ticks, label)

plt.show()
