import numpy as np 

k = 1.38e-23
q = 1.6e-19
T = 300 # Given in LTspice output log 

Vt = k*T/q
Ic = 4.98e-3
Ib = 0.000277482
rpi = Vt/Ib
gm = Ic/Vt 
print("Vt: ", Vt)
#re = Vt/Ie 
#print("rpi: ", rpi)
print("gm: ", gm)
#print("re: ", re)

