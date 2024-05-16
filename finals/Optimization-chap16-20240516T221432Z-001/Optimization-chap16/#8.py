 #Find the linear interpolation at x = 1.5 based on the data x = [0, 1, 2], y = [1, 3,
#2]. Verify the result using SciPy’s function interp1d.
#Since 1 <x< 2, we use the second and third data points to compute the linear interpolation.
#Plugging in the corresponding values gives

import numpy as np
from scipy.interpolate import interp1d

# Given data points
x_data = np.array([0, 1, 2])
y_data = np.array([1, 3, 2])

# Find the indices of the data points surrounding x = 1.5
idx_left = np.where(x_data <= 1.5)[0][-1]  # Index of the left data point
idx_right = np.where(x_data > 1.5)[0][0]   # Index of the right data point

# Compute the linear interpolation at x = 1.5
y_interp = y_data[idx_left] + (y_data[idx_right] - y_data[idx_left]) * (1.5 - x_data[idx_left]) / (x_data[idx_right] - x_data[idx_left])

# Print the result of linear interpolation
print("Linear interpolation at x = 1.5:", y_interp)

# Verify the result using scipy's interp1d function
f = interp1d(x_data, y_data, kind='linear')
y_interp_scipy = f(1.5)

# Print the result obtained using interp1d
print("Result obtained using interp1d:", y_interp_scipy)
