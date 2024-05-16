import numpy as np

# Given data
t = np.array([0, 25, 50, 75, 100, 125])  # time in seconds
y = np.array([0, 32, 58, 78, 92, 100])  # distance in km

# Calculate velocity (first derivative of y with respect to t)
v = np.zeros_like(y, dtype=float)
v[1:-1] = (y[2:] - y[:-2]) / (t[2:] - t[:-2])  # Central difference for interior points
v[0] = (y[1] - y[0]) / (t[1] - t[0])          # Forward difference for the first point
v[-1] = (y[-1] - y[-2]) / (t[-1] - t[-2])      # Backward difference for the last point

# Calculate acceleration (second derivative of y with respect to t)
a = np.zeros_like(y, dtype=float)
a[1:-1] = (y[2:] - 2*y[1:-1] + y[:-2]) / ((t[2:] - t[:-2])/2)**2  # Central difference for interior points
a[0] = (y[2] - 2*y[1] + y[0]) / (t[1] - t[0])**2                 # Forward difference for the first point
a[-1] = (y[-1] - 2*y[-2] + y[-3]) / (t[-1] - t[-2])**2           # Backward difference for the last point

# Print the results
print("Time (s):", t)
print("Distance (km):", y)
print("Velocity (km/s):", v)
print("Acceleration (km/s^2):", a)
