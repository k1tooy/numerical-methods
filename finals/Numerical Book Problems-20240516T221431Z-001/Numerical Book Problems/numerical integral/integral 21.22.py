#21.22 The work produced by a constant temperature, pressurevolume thermodynamic process can be computed as W 5 # p dV
#where W is work, p is pressure, and V is volume. Using a combination of the trapezoidal rule, Simpson’s 1y3 rule, and Simpson’s
#3y8 rule, use the following data to compute the work in kJ (kJ 5 kN ? m):

import numpy as np

# Given data
pressure = np.array([336, 294.4, 266.4, 260.8, 260.5, 249.6, 193.6, 165.6])  # in kPa
volume = np.array([0.5, 2, 3, 4, 6, 8, 10, 11])  # in m^3

# Number of data points
n = len(pressure)

# Initialize work
work = 0

# Apply Trapezoidal rule for the first interval
work += (volume[1] - volume[0]) * (pressure[0] + pressure[1]) / 2

# Apply Simpson's 1/3 rule for the next six intervals
for i in range(1, n - 3, 2):
    h = volume[i+2] - volume[i]
    work += h * (pressure[i] + 4*pressure[i+1] + pressure[i+2]) / 6

# Apply Simpson's 3/8 rule for the last three intervals
h = volume[-1] - volume[-4]
work += 3*h * (pressure[-4] + 3*pressure[-3] + 3*pressure[-2] + pressure[-1]) / 8

# Convert work to kJ (since pressure is in kPa and volume is in m^3, the result is in kJ)
work_kJ = work

print(f'The work produced by the process is {work_kJ:.2f} kJ')
