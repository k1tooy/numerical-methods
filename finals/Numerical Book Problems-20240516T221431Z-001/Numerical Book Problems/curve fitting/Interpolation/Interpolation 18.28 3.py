#The following data defi ne the sea-level concentration of 
 #dissolved oxygen for fresh water as a function of temperature:
# T,°C 0 8 16 24 32 40
# o,mg/L 14.62111.843 9.870 8.418 7.305 6.413
 #Estimate o(27) using (c) cubic splines.

import numpy as np
from scipy.interpolate import CubicSpline

# Data
temperature = np.array([0, 8, 16, 24, 32, 40])
oxygen = np.array([14.621, 11.843, 9.870, 8.418, 7.305, 6.413])

# Cubic splines interpolation
cubic_spline = CubicSpline(temperature, oxygen)
estimated_oxygen_spline = cubic_spline(27)
print(f"Estimated oxygen concentration at 27°C using cubic splines: {estimated_oxygen_spline:.3f} mg/L")
