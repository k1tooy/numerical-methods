 #Given four data points (xi, yi) and the parameters for a cubic polynomial y(x) ˆ = ax3 + bx2 + cx +
#d, what will be the total error associated with the estimation function y(x) ˆ ? Can we place another
#data point (x,y) such that no additional error is incurred for the estimation function?

#                      4/5

import numpy as np

# Define the cubic polynomial function
def cubic_polynomial(x, params):
    a, b, c, d = params
    y = a * x**3 + b * x**2 + c * x + d
    return y

# Define a function to calculate the total error
def total_error(data, params):
    total_error = 0
    for x, y in data:
        estimated_y = cubic_polynomial(x, params)
        error = (y - estimated_y)**2  # Squared error
        total_error += error
    return total_error

# Given data points (xi, yi)
data = [(1, 2), (2, 5), (3, 10), (4, 17)]

# Parameters for the cubic polynomial y(x) = ax^3 + bx^2 + cx + d
params = [1, 1, 1, 1]

# Calculate the total error associated with the estimation function
error = total_error(data, params)
print("Total error:", error)

# Find the optimal parameters that minimize the total error
from scipy.optimize import minimize

# Define a function to minimize the total error by adjusting parameters
def minimize_error(params):
    return total_error(data, params)

# Perform optimization to find the optimal parameters
optimal_params = minimize(minimize_error, params).x

# Calculate the total error associated with the optimized parameters
optimal_error = total_error(data, optimal_params)
print("Optimized total error:", optimal_error)

# Check if adding a new data point reduces the error
new_data_point = (5, 26)  # New data point to be added
new_data = data + [new_data_point]

# Calculate the error after adding the new data point
new_error = total_error(new_data, optimal_params)

if new_error <= optimal_error:
    print("Adding the new data point does not incur additional error.")
else:
    print("Adding the new data point incurs additional error.")

print("New total error:", new_error)
