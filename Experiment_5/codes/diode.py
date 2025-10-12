
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

Is_fixed = 0.0154e-15  # 0.0154 fA in amps
n_fixed = 1.0

# Given experimental saturation


Vs = np.array([0.0, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0])
Vd = np.array([0.0, 0.143, 0.250, 0.399, 0.478, 0.519, 0.544, 0.560, 0.571, 0.579, 0.588, 0.595, 0.601, 0.608, 0.614, 0.617, 0.621, 0.626, 0.629, 0.633, 0.636, 0.639, 0.641, 0.644, 0.647, 0.649, 0.652])
R = 1e3
Id = (Vs-Vd)/R 
V_data = Vd
I_data = Id

#V_data = np.array([859.78115e-3, 857.81902e-3, 855.70192e-3 , 850.88754e-3, 841.49939e-3, 832.6841e-3,
#819.42105e-3, 792.17714e-3, 746.76347e-3, 499.99619e-3, 300.00001e-3, 100e-3])
#I_data = np.array([4.1402187e-3, 3.9415108e-3, 3.6435737e-3, 3.0482474e-3, 2.1572786e-3, 1.5656289e-3,
#977.86169e-6, 400.97695e-6, 130.11476e-6, 181.5441e-9, 80.541684e-12, 235.08973e-15])
#V_data = np.array([
#    857.81902e-3, 855.70192e-3, 850.88754e-3,
#    841.49939e-3, 832.6841e-3, 819.42105e-3, 792.17714e-3
#])
#I_data = np.array([
#    3.9415108e-3, 3.6435737e-3, 3.0482474e-3,
#    2.1572786e-3, 1.5656289e-3, 977.86169e-6, 400.97695e-6
#])

# Shockley diode function
def shockley(V, Is, n):
    Vt = 0.025875  # Typical value in volts at room temperature (~25°C)
    return Is * (np.exp(V / (n * Vt)) - 1)

# Fit curve to data
initial_guess = [1e-12, 1.5]  # Initial guesses for Is and n
popt, pcov = curve_fit(shockley, V_data, I_data, p0=initial_guess)

Is_fit, n_fit = popt
print(f"Saturation current Is: {Is_fit:.3e} A")
print(f"Ideality factor n: {n_fit:.3f}")

I_fit = shockley(np.linspace(0, V_data[-1], int(1e5)), Is_fit, n_fit)



# Plot data and fit
plt.figure(figsize=(8,6))
plt.plot(V_data, I_data, 'o', label="Data")
plt.plot(np.linspace(0, V_data[-1], int(1e5)), I_fit, '-', label="Shockley Fit", color="orange")
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.title('Shockley Diode Equation Fit')
plt.legend()
plt.grid(True)
plt.show()

