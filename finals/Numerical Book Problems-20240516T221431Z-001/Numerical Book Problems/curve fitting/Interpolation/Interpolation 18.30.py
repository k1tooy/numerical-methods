#Temperatures are measured at various points on a heated 
#plate (Table P18.30). Estimate the temperature at (a) x 5 4, y 5 3.2, 
#and (b) x 5 4.3, y 5 2.7.

import numpy as np

# Bilinear interpolation function
def bilinear_interpolation(x, y, points):
    points = sorted(points)  # Sort points by x, then by y
    (x1, y1, z1), (x1, y2, z3), (x2, y1, z2), (x2, y2, z4) = points

    if x1 == x2 or y1 == y2:
        raise ValueError("The provided points do not form a proper rectangle")

    return (
        z1 * (x2 - x) * (y2 - y) +
        z2 * (x - x1) * (y2 - y) +
        z3 * (x2 - x) * (y - y1) +
        z4 * (x - x1) * (y - y1)
    ) / ((x2 - x1) * (y2 - y1))

# Temperature data
x_vals = np.array([0, 2, 4, 6, 8])
y_vals = np.array([0, 2, 4, 6, 8])
temperatures = np.array([
    [100.00, 90.00, 80.00, 70.00, 60.00],
    [85.00, 64.49, 53.50, 48.15, 50.00],
    [70.00, 48.90, 38.43, 35.00, 40.00],
    [55.00, 38.78, 30.39, 27.07, 30.00],
    [40.00, 35.00, 30.00, 25.00, 20.00]
])

# Function to find the enclosing rectangle points
def get_enclosing_points(x, y, x_vals, y_vals, temperatures):
    x1_idx = np.searchsorted(x_vals, x) - 1
    x2_idx = x1_idx + 1
    y1_idx = np.searchsorted(y_vals, y) - 1
    y2_idx = y1_idx + 1

    x1, x2 = x_vals[x1_idx], x_vals[x2_idx]
    y1, y2 = y_vals[y1_idx], y_vals[y2_idx]

    z11 = temperatures[y1_idx, x1_idx]
    z12 = temperatures[y1_idx, x2_idx]
    z21 = temperatures[y2_idx, x1_idx]
    z22 = temperatures[y2_idx, x2_idx]

    return [(x1, y1, z11), (x1, y2, z21), (x2, y1, z12), (x2, y2, z22)]

# (a) Estimate the temperature at (x = 4, y = 3.2)
x, y = 4, 3.2
points = get_enclosing_points(x, y, x_vals, y_vals, temperatures)
temperature_a = bilinear_interpolation(x, y, points)
print(f"Estimated temperature at (x = 4, y = 3.2): {temperature_a:.2f}°C")

# (b) Estimate the temperature at (x = 4.3, y = 2.7)
x, y = 4.3, 2.7
points = get_enclosing_points(x, y, x_vals, y_vals, temperatures)
temperature_b = bilinear_interpolation(x, y, points)
print(f"Estimated temperature at (x = 4.3, y = 2.7): {temperature_b:.2f}°C")
