import numpy as np

# For NMOS
Id = 4.98997e-5
Vto = 0.7
Vgs = 1 - 0.151664
lamb = 0.01

gm = 2*Id/(Vgs-Vto)
ro_1 = 1/(lamb*Id)
print("ro_1: ", ro_1)

# For PMOS

#Id = 5.01692e-5
lamb = 0.01
ro_2 = 1/(lamb*Id)
print("ro_2: ", ro_2)

ro = (ro_1*ro_2)/(ro_1+ro_2)

f = 1/(2*np.pi*ro*1e-12)
print("f: ", f)

tau = ro*1e-6
print("tau: ", tau)
#t = 11.357096e-6
#t = 3.9066178e-6
#t=  7.4026044e-6
#t = 460.45311e-3
#t = 0.20445311
#vfinal = 922.35386e-3
#vfinal = 1.0999779-1.0989504
#print("V_final=", vfinal)


#v = vfinal*(1-np.exp(-t/tau))
#print(f"transient at t = {t} is, {v+1.0989504} V")

A = gm*ro
print(A)

rtail = 5004882.2626472125

CMRR = 20*np.log10(2*gm*rtail)
print("CMRR: ", CMRR, "dB")
