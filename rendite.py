import matplotlib.pyplot as plt
import numpy as np

jahreskapital = 1200
rendite = 0.08
zeit = 10

endwert = 0
for i in range(1, zeit + 1):
    endwert += (jahreskapital * (1 + rendite)**i)

print("Bei ", jahreskapital, " Euro Kapital, nach ", i, " Jahren: ", endwert)

print(  "Davon Gewinn durch Rendite: ", endwert - zeit * jahreskapital,
        " (Inflation beruecksichtigt: ",
        (endwert - zeit * jahreskapital)*0.97**10,
        ")" )
