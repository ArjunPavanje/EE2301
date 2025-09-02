import numpy as np

ic = 0.0144928 
ib = 4.90439e-5 
ie = 0.0145419	  
Vt = 0.025875
RE = 500  
RL = 500 
RB1 = 50 
RB2 = 200
re = Vt/ie
beta = ic/ib
Re = RE*RL/(RE+RL)
Ri = beta*RE 
RB = RB1*RB2/(RB1+RB2)
Ri = RB*Ri/(RB+Ri)
r = Re*beta 
Ri = (RB*r)/(RB+r)
Rs = 500
Ro = Re*re/(Re+re)
A =  Re/(Re + re)
print("rin: ", Ri)
print("Ro: ", Ro)
print("gain: ", A)
