import numpy as np

n = 1.907
Is = 8.019e-9

Vs = 5
Vd = 0.652

Vt = 0.025875
R = 1000

Id = (Vs-Vd)/R
rd = n*Vt/Id

Vm = 0.5
A = Vm*rd/(rd+R)

g1 = Is*np.exp(Vd/(n*Vt))/(n*Vt)
Amp = A*g1
print("Amplitude: ", Amp)



Vm = 3.75
A = Vm*rd/(rd+R)
g2 = Is*np.exp(Vd/(n*Vt))/((n*Vt)**2)

Amp = 1/2*g2*(A**2)
print("Amplitude: ", Amp)




