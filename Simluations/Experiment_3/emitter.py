import numpy as np

ic = 2.67e-3 # Collector current 
ib = 7.97e-6 # Base current 
Vt = 0.025875 # kT/q
rc = 80 # RC in circuit 
rl = 1e3 # Load resistance, RL in circuit  
beta = ic/ib # beta 
gm = ic/Vt # transconductance 
re = 1/gm # re'   
Ro = rc*rl/(rc+rl)
rpi = beta/gm
rB = 500*100/600
Ri = rpi*rB/(rpi+rB)
print("Ri ", Ri)
A = gm*Ro
print("r0: ", Ro)
print("gain: ", A)
