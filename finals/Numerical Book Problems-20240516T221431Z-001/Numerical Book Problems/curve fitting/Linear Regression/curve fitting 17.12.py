#17.12 An investigator has reported the data tabulated below for an
#experiment to determine the growth rate of bacteria k (per d), as a
#function of oxygen concentration c (mg/L). It is known that such
#data can be modeled by the following equation:

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Given data
c = np.array([0.5, 0.8, 1.5, 2.5, 4.0])
k = np.array([1.1, 2.4, 5.3, 7.6, 8.9])

# Transform the data
x = 1 / (c**2)
y = 1 / k

# Define the linear model
def linear_model(x, a, b):
    return a + b * x

# Perform linear regression using curve_fit
popt, pcov = curve_fit(linear_model, x, y)

# Extract the parameters
a = popt[0]
b = popt[1]

# Calculate k_max and c_s from the linear parameters a and b
k_max = 1 / a
c_s = b / a

print(f"Estimated k_max: {k_max}")
print(f"Estimated c_s: {c_s}")

# Predict the growth rate at c = 2 mg/L
c_pred = 2
k_pred = (k_max * c_pred**2) / (c_s + c_pred**2)
print(f"Predicted growth rate at c = 2 mg/L: {k_pred}")

# Plot the data and the fit
plt.scatter(x, y, label='Data')
plt.plot(x, linear_model(x, *popt), label='Fitted line', color='red')
plt.xlabel('1/c^2')
plt.ylabel('1/k')
plt.legend()
plt.show()
