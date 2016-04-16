import numpy as np
import matplotlib.pyplot as plt

rA = 40e3
rB = 60e3
rC = 40e3
rD = 30e3
cA = 30e-15
cB = 2e-15
cC = 8e-15
cD = 1e-15
RCa = 1.260e-9
RCb = .126e-9
RCc = RCa / 3.8
RCd = RCb / 3.8
x = np.linspace(-10, 10, 100)
omega = np.linspace(1e6, 1e12, 1e6)
# phi1 = -2 * np.arctan(omega*r1*c1) * 90
# phi2 = -2 * np.arctan(omega*r2*c2) * 90

delta_phi = -360 / np.pi * (  np.arctan(omega * RCa) + np.arctan(omega*RCb)
                            - np.arctan(omega * RCc) - np.arctan(omega * RCd) )
# delta_phi = -2 * ( np.arctan(omega * rA*cA) + np.arctan(omega*rB*cB) ) * 180 / np.pi

# plt.plot(omega, phi)
plt.semilogx(omega, delta_phi)
# plt.plot(x, np.arctan(x)*180/np.pi)
plt.grid(True)
plt.show()
