import numpy as np

id = 16.78e-3 # Drain current
r0 = 80 # Ro = Rd 
kp = 76.2004 # Property of MOSFET
#gm = np.sqrt(2*kp*id)
Vgs = 18.1818 - 16.780 # VG-VS 
Vth = 1.38 #Vt0, property of MOSFET 
gm = 2*id/(Vgs-Vth) # transconductance
A = gm*r0
RG1 = 50
RG2 = 500
Ro = r0 # Output Resistance
Ri = RG1*RG2/(RG1+RG2) # Input Resistance
print("gain: ", A)
print("Ri: ", Ri)
print("Ro: ", Ro)
