import numpy as np
import matplotlib.pyplot as plt

RCa = 1.255e-9
faktorAB = 7.8
faktorAC = faktorAB / 2.285714
faktorBD = faktorAC
RCb = RCa / faktorAB
RCc = RCa / faktorAC
RCd = RCb / faktorBD

x = np.linspace(-10, 10, 100)
omega = np.linspace(1e6, 1e12, 1e6)

delta_phi = -360 / np.pi * (  np.arctan(omega * RCa) + np.arctan(omega*RCb)
                            - np.arctan(omega * RCc) - np.arctan(omega * RCd) )

plt.semilogx(omega, delta_phi)
plt.grid(True)
plt.show()
