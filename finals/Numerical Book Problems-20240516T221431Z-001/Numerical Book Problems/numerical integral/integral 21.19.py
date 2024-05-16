#21.19 The following data was collected for a cross-section of a
#river (y 5 distance from bank, H 5 depth, and U 5 velocity):

import numpy as np

# Given data
y = np.array([0, 1, 3, 5, 7, 8, 9, 10])
H = np.array([0, 1.5, 3, 3.5, 3.2, 3, 2.2, 0])
U = np.array([0, 0.1, 0.12, 0.2, 0.25, 0.3, 0.15, 0])

# (a) Average depth
average_depth = np.trapz(H, y) / (y[-1] - y[0])
print(f"Average depth: {average_depth:.2f} meters")

# (b) Cross-sectional area
cross_sectional_area = np.trapz(H, y)
print(f"Cross-sectional area: {cross_sectional_area:.2f} square meters")

# (c) Average velocity
average_velocity = np.trapz(U * H, y) / cross_sectional_area
print(f"Average velocity: {average_velocity:.2f} meters/second")

# (d) Flow rate
flow_rate = np.trapz(H * U, y)
print(f"Flow rate: {flow_rate:.2f} cubic meters/second")
