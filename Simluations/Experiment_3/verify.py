import numpy as np

#id = 92.70e-3
#id = 115.78e-3
#id = 91.03e-3
id = 17.6195
#r0 = 80
rs = 1000
kp = 76.2004
#kp = 160.4
Vgs = 19.801-17.6195
Vth = 2.16
#gm = np.sqrt(kp*id)
gm = 2*id/(Vgs - Vth)
#A = gm*r0
#A = r0*(2*id/(Vgs-Vth))
A = gm*rs/(1+(gm*rs))
print("gain: ", A)
