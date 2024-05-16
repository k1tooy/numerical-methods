import numpy as np

# Data
temperature = np.array([0, 8, 16, 24, 32, 40])
oxygen = np.array([14.621, 11.843, 9.870, 8.418, 7.305, 6.413])

# Linear interpolation
def linear_interpolation(x, xp, yp):
    return np.interp(x, xp, yp)

estimated_oxygen_linear = linear_interpolation(27, temperature, oxygen)
print(f"Estimated oxygen concentration at 27°C using linear interpolation: {estimated_oxygen_linear:.3f} mg/L")
