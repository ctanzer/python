import numpy as np
import matplotlib.pyplot as plt

# realtive Dehnung aus Kraft und Geometrie berechnen
tonnen = np.linspace(0, 50)
kraft = tonnen * 10000 # in Newton
flaeche = 0.04 # in Quadratmetern
elastizitaetsmodul = 180e9 # in Pascal
stuetzenzahl = 4

epsilon = kraft / (flaeche * elastizitaetsmodul * stuetzenzahl)

plt.plot(tonnen, epsilon)
plt.grid(True)
plt.show()