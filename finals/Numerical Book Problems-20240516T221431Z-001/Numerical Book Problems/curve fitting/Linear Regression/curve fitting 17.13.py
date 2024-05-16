#An investigator has reported the data tabulated below. It is known that such data can be modeled by the following equation x 5 e(y2b)ya where a and b are parameters. Use a transformation to linearize this
#equation and then employ linear regression to determine a and b.
#Based on your analysis predict y at x 5 2.6.

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Given data
x = np.array([1, 2, 3, 4, 5])
y = np.array([0.5, 2, 2.9, 3.5, 4])

# Transform the data
x_transformed = np.log(x)

# Define the linear model
def linear_model(x, a, b):
    return a * x + b

# Perform linear regression using curve_fit
popt, pcov = curve_fit(linear_model, x_transformed, y)

# Extract the parameters
a = popt[0]
b = popt[1]

print(f"Estimated a: {a}")
print(f"Estimated b: {b}")

# Predict the y value at x = 2.6
x_pred = 2.6
y_pred = a * np.log(x_pred) + b
print(f"Predicted y at x = 2.6: {y_pred}")

# Plot the data and the fit
plt.scatter(x_transformed, y, label='Data')
plt.plot(x_transformed, linear_model(x_transformed, *popt), label='Fitted line', color='red')
plt.xlabel('ln(x)')
plt.ylabel('y')
plt.legend()
plt.show()
