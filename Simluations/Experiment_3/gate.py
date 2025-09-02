import numpy as np

id = 2.293e-3 # Drain current 
rd = 500 # RD in circuit 
rl = 10e3 # Load resistance, RL in circuit 
reff = rd*rl/(rd+rl)
Vgs = 13.6363-11.466 # VG - VS
Vth = 2.16 # Vto, property of MOSFET 
gm = 2*id/(Vgs - Vth) # transconductance
rs = 5e3 # RS in circuit  
Ri =  (rs/gm)/(rs + 1/gm) # Input resistance 
Ro = rd  # Output resistance 
A = gm*reff # gain 
print("gain: ", A)
print("Ri: ", Ri)
print("Ro: ", Ro)
