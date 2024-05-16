#17.25 The following data show the relationship between the viscosity of SAE 70 oil and temperature. After taking the log of the
#data, use linear regression to fi nd the equation of the line that best
#fi ts the data and the r 2 value.

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Given data
temperature = np.array([26.67, 93.33, 148.89, 315.56])
viscosity = np.array([1.35, 0.085, 0.012, 0.00075])

# Transform the viscosity data by taking the natural logarithm
log_viscosity = np.log(viscosity)

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(temperature, log_viscosity)

# Print the results
print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R-squared: {r_value**2}")

# Plot the data and the regression line
plt.scatter(temperature, log_viscosity, label='Data')
plt.plot(temperature, slope * temperature + intercept, color='red', label='Fitted line')
plt.xlabel('Temperature (°C)')
plt.ylabel('ln(Viscosity) (ln(N·s/m²))')
plt.legend()
plt.show()
