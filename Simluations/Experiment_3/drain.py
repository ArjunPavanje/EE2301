import numpy as np

id = 16e-3 # Drain current
rs = 1e3 # RS in circuit
rl = 1e3 # Load Resistance (RL in circuit)
RG1 = 50
RG2 = 500
r0 = (rs*rl)/(rs+rl) # 
Vgs = 18.181818 - 16.000 # VG - VS 
Vth = 2.16 # Vto, property of MOSFET
gm = 2*id/(Vgs-Vth) # transconductance 
Ri = RG1*RG2/(RG1+RG2) # Input resistance 
Ro = (rs/gm)/(rs + 1/gm)

A = gm*r0/(1+gm*r0)

print("gain: ", A)
print("Ri: ", Ri)
print("Ro: ", Ro)
