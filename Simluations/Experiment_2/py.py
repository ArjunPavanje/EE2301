import numpy as np 

k = 1.38e-23
q = 1.6e-19
T = 300 # Given in LTspice output log 
N = 1.752 # Property of diode

Vt = k*T/q
Vd = 500.626e-3

Id = 157.928e-6 
Is = Id/(np.exp(Vd/(N*Vt))-1)

print(N*Vt/Id)
print(Is)
