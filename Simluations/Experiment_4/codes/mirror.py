import numpy as np

kp = 90e-6
Vto = 0.07
I_target = 100e-6
Vs = 5

Vg = Vd = np.sqrt(2*I_target/kp)+Vto

R = (Vs - Vd)/I_target
print("R = ", R, " Ohms")

lamb = 0.001
Id = 9.98029e-05
r0_5 = 1/(lamb*Id)

print("ro5 = ", r0_5)

Id = 0.000100002
r0_6 = 1/(lamb*Id)

print("ro6 = ", r0_6)

r0 = (r0_5*r0_6)/(r0_5+r0_6)
print("rtail: ", r0)

