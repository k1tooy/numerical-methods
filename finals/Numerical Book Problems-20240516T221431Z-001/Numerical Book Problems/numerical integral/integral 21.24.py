#21.24 The total mass of a variable density rod is given by
#m 5 #
#L
#0
#r(x)Ac(x) dx
#where m 5 mass, r (x) 5 density, Ac(x) 5 cross-sectional area, x 5
#distance along the rod, and L 5 the total length of the rod. The following data have been measured for a 10-m length rod
# Determine the mass in kilograms to the best possible accuracy

import numpy as np

# Given data
x = np.array([0, 2, 3, 4, 6, 8, 10])  # x in meters
rho = np.array([4.00, 3.95, 3.89, 3.80, 3.60, 3.41, 3.30]) * 1000  # density in kg/m³
Ac = np.array([100, 103, 106, 110, 120, 133, 150]) * 0.0001  # cross-sectional area in m²

# Number of data points
n = len(x)

# Initialize mass
mass = 0

# Apply Trapezoidal rule for the first interval
mass += (x[1] - x[0]) * (rho[0] * Ac[0] + rho[1] * Ac[1]) / 2

# Apply Simpson's 1/3 rule for the next five intervals
for i in range(1, n - 2, 2):
    h = x[i+2] - x[i]
    mass += h * (rho[i] * Ac[i] + 4 * rho[i+1] * Ac[i+1] + rho[i+2] * Ac[i+2]) / 6

# Apply Trapezoidal rule for the last interval if needed
if (n - 1) % 2 == 0:
    mass += (x[-1] - x[-2]) * (rho[-1] * Ac[-1] + rho[-2] * Ac[-2]) / 2
else:
    h = x[-1] - x[-3]
    mass += h * (rho[-3] * Ac[-3] + 4 * rho[-2] * Ac[-2] + rho[-1] * Ac[-1]) / 6

print(f'The mass of the rod is {mass:.2f} kg')
