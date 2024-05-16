 #Write a function my_lin_regression(f, x, y) where f is a list containing function objects to
#basis functions, and x and y are arrays containing noisy data. Assume that x and y are the same size.
#Let an estimation function for the data contained in x and y be defined as y(x) ˆ = β(1) · f1(x) +
#β(2) · f2(x) +···+ β(n) · fn(x), where n is the length of f. Your function should compute beta
#according to the least squares regression formula.

#                5/5

import numpy as np

def my_lin_regression(f, x, y):
    """
    Perform linear regression to estimate parameters beta for given noisy data (x, y)
    and basis functions f.

    Args:
    - f: List of function objects representing basis vectors
    - x: Array of independent variable values
    - y: Array of dependent variable values corresponding to x

    Returns:
    - beta: Array of parameters for the linear regression
    """
    # Determine the number of data points
    n = len(x)

    # Determine the number of basis functions
    p = len(f)

    # Initialize the design matrix with zeros
    X = np.zeros((n, p))

    # Populate the design matrix by evaluating each basis function at each x value
    for i in range(n):
        for j in range(p):
            X[i, j] = f[j](x[i])

    # Perform least squares regression to estimate the parameters beta
    beta = np.linalg.lstsq(X, y, rcond=None)[0]

    return beta

# Example usage:
# Define basis functions
def f1(x):
    return x

def f2(x):
    return np.sin(x)

# Generate noisy data
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x) + np.random.normal(0, 0.1, 100)  # Adding Gaussian noise to sin function

# Perform linear regression
beta = my_lin_regression([f1, f2], x, y)

print("Estimated parameters beta:", beta)
