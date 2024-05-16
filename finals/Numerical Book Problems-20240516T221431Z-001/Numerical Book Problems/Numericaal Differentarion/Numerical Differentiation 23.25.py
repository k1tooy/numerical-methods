import numpy as np

# Given data
t = np.array([0, 1, 5, 8])  # time in seconds
v = np.array([0, 1, 8, 16.4])  # volume in cm^3

# We need to estimate the flow rate (dV/dt) at t = 7 s
# Use the central difference method for interior points
# First find the indices surrounding t = 7
idx_before = np.searchsorted(t, 7) - 1
idx_after = idx_before + 1

# Linear interpolation to find the volume at t = 7
V_7 = v[idx_before] + (v[idx_after] - v[idx_before]) * (7 - t[idx_before]) / (t[idx_after] - t[idx_before])

# Now we have a new point at t = 7 with interpolated volume
t_new = np.insert(t, idx_after, 7)
v_new = np.insert(v, idx_after, V_7)

# Estimate the flow rate at t = 7 using central difference
def central_difference(x, y, idx):
    return (y[idx + 1] - y[idx - 1]) / (x[idx + 1] - x[idx - 1])

flow_rate_7 = central_difference(t_new, v_new, idx_after)

# Print the result
print("The estimated flow rate at t = 7 s is {:.2f} cm^3/s".format(flow_rate_7))
