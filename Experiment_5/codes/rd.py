import numpy as np


# Vs values around bias point
Vs1 = 3+960e-3
Vs2 = 3-960e-3

# Vd values around bias point
Vd1 = 3+18e-3
Vd2 = 3-18e-3

# Diode parameters
n = 1.907
Vt = 0.025875
R = 1000

# Id around bias point 
Id1 = (Vs1-Vd1)/R
Id2 = (Vs2-Vd2)/R
# Id at bias point
Id = (3-0.616)/R
#print(Id)

# Calculating small signal parameter rd
rd_th = n*Vt/np.abs(Id) # theoretical
rd = (Vd2-Vd1)/(Id2-Id1)

print("rd: ", rd)
print("rd (theoretical): ", rd_th)


'''
Vs1 = 3+150e-3
Vs2 = 3-152e-3

Vd1 = 3+148e-3
Vd2 = 3-148e-3

'''
