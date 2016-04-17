delta_f = -6000
f_s = 1575420000

c = 299792458

v = c * (1 - (1/(1-(delta_f/f_s))))

print(v, " m/s")
print(v/3.6, " km/h")
