 #Repeat the multivariate calculus derivation of the least squares regression formula for an estimation
#function y(x) ˆ = ax2 + bx + c, where a,b, and c are the parameters.

#3  1/5

import numpy as np
from scipy.optimize import minimize

def quadratic_regression(params, x, y):
    a, b, c = params
    y_pred = a * x**2 + b * x + c
    return np.sum((y - y_pred)**2)

# Sample data
x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([3, 6, 8, 10, 12])

# Initial guess for parameters
initial_guess = [1, 1, 1]

# Minimize the objective function
result = minimize(quadratic_regression, initial_guess, args=(x_data, y_data))

# Extract optimized parameters
a_opt, b_opt, c_opt = result.x

print("Optimized parameters:")
print("a =", a_opt)
print("b =", b_opt)
print("c =", c_opt)