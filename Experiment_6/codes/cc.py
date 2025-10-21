import numpy as np
import matplotlib.pyplot as plt

# V_E = -5.0
V_CE_1 = np.array([0, 0.028, 0.07, 0.116, 0.167, 0.266, 1.449, 2.928, 4.911, 6.91])
V_R_1 = np.array([0, 0.018, 0.021, 0.022, 0.022, 0.022, 0.023, 0.025, 0.029, 0.033])
R = 150
I_E_1 = V_R_1/R

# V_E = -7.5
V_CE_2 = np.array([0, 0.016, 0.046, 0.087, 0.165, 0.261, 0.549, 1.031, 3.441])
V_R_2 = np.array([0, 0.194, 0.260, 0.304, 0.319, 0.322, 0.325, 0.336, 0.34])
R = 150
I_E_2 = V_R_2/R

# V_E = -2.5
V_CE_3 = np.array([0, 0.067, 0.255, 0.352, 0.548, 0.844, 1.333, 2.8])
V_R_3 = np.array([0, 0.095, 0.104, 0.104, 0.106, 0.107, 0.112, 0.12])
R = 150
I_E_3 = V_R_3/R


# V_C = -3
# - 0.928
#V_BE_1 = -np.array([0, -0.197, 0.394, -0.542, -0.589, -0.673, -0.752, -0.852])
#V_R_4 = np.array([0, 0, 0, 0.001, 0.01, 0.053, 0.128, 0.216])
V_CB_1 = np.array([0, 0.196, 0.583, 0.644, 0.714, 0.748, 0.8, 0.84])
V_R_4 = -np.array([0, 0, 0.006, 0.008, 0.104, 0.548, 1.631, 3.086])
I_B_1 = V_R_4/R

# V_C = -2
V_CB_2 = np.array([0, 0.196, 0.583, 0.646, 0.676, 0.714, 0.785, 0.817])
V_R_5 = -np.array([0, 0, 0.006, 0.033, 0.082, 0.108, 1.626, 3.095])
I_B_2 = V_R_5/R

# V_C = -1
V_CB_3 = np.array([0, 0.196, 0.582, 0.674, 0.715, 0.75, 0.82, 0.86])
V_R_6 = -np.array([0, 0, 0.006, 0.084, 0.103, 0.549, 1.624, 3.086])
I_B_3 = V_R_6/R

plt.figure()
plt.plot(V_CE_1, I_E_1, marker='o', color="red", label="VE = 0.6")
plt.plot(V_CE_2, I_E_2, marker='o', color="blue", label="VE = 0.7")
plt.plot(V_CE_3, I_E_3, marker='o', color="green", label="VE = 0.650")
plt.legend()
plt.show()

plt.figure()
plt.plot(-V_CB_1 + 0.1, -I_B_1, marker='o', color="red", label="VC = 0.6")
plt.plot(-V_CB_2, -I_B_2, marker='o', color="blue", label="VC = 0.5")
plt.plot(-V_CB_3 - 0.05, -I_B_3, marker='o', color="green", label="VC = -1")
plt.legend()
plt.show()
