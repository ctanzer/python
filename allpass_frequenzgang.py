import numpy as np
import matplotlib.pyplot as plt

RCa = 1.260e-9
RCb = .126e-9
RCc = RCa / 3.8
RCd = RCb / 3.8
x = np.linspace(-10, 10, 100)
omega = np.linspace(1e6, 1e12, 1e6)

delta_phi = -360 / np.pi * (  np.arctan(omega * RCa) + np.arctan(omega*RCb)
                            - np.arctan(omega * RCc) - np.arctan(omega * RCd) )
                            
plt.semilogx(omega, delta_phi)
plt.grid(True)
plt.show()
