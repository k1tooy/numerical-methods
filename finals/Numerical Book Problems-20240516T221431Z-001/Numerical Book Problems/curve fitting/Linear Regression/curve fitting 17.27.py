#17.27 The concentration of E. coli bacteria in a swimming area is monitored after a storm:

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Given data
t_data = np.array([4, 8, 12, 16, 20, 24])
c_data = np.array([1600, 1320, 1000, 890, 650, 560])

# Define the model function
def model(t, c0, k):
    return c0 * np.exp(-k * t)

# Use curve_fit to find the best fit parameters c0 and k
params, covariance = curve_fit(model, t_data, c_data)
c0, k = params

# Print the estimated parameters
print(f"Estimated c0 (concentration at t=0): {c0:.2f} CFU/100 mL")
print(f"Estimated k (decay constant): {k:.4f} per hour")

# Calculate the time at which the concentration will reach 200 CFU/100 mL
target_concentration = 200
time_target = np.log(c0 / target_concentration) / k
print(f"Time at which the concentration reaches 200 CFU/100 mL: {time_target:.2f} hours")

# Plot the data and the fitted curve
t_fit = np.linspace(0, 30, 100)
c_fit = model(t_fit, c0, k)

plt.scatter(t_data, c_data, label='Data')
plt.plot(t_fit, c_fit, label='Exponential Fit', color='red')
plt.axhline(y=200, color='green', linestyle='--', label='200 CFU/100 mL')
plt.axvline(x=time_target, color='blue', linestyle='--', label=f'target time = {time_target:.2f} hours')
plt.xlabel('Time (hours)')
plt.ylabel('Concentration (CFU/100 mL)')
plt.legend()
plt.title('E. coli Bacteria Concentration After Storm')
plt.show()
