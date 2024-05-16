#Newton's Method Optimization

import numpy as np

# Define the function and its derivative
def f(x):
    return 2 * np.sin(x) - x**2 / 10

def f_prime(x):
    return 2 * np.cos(x) - x / 5

# Implement Newton's method to find the maximum
def newton_max(f_prime, x0, tol=1e-6, max_iter=100):
    x = x0
    for _ in range(max_iter):
        x_new = x - f_prime(x) / f_prime(f_prime(x))
        if abs(x_new - x) < tol:
            break
        x = x_new
    return x

# Initial guess
x0 = 2.5

# Find the maximum using Newton's method
x_max = newton_max(f_prime, x0)

# Print the result
print("Approximation of the maximum:", x_max)
print("Value of the function at the maximum:", f(x_max))
