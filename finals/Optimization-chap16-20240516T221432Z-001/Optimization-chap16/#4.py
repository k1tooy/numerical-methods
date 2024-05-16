# Write a function my_ls_params(f, x, y) where x and y are arrays of the same size containing
#experimental data, and f is a list with each element a function object to a basis vector of the estimation function. The output argument, beta, should be an array of the parameters of the least squares
#regression for x, y, and f.

#4           2/5

import numpy as np

def my_ls_params(f, x, y):
    """
    Perform least squares regression to estimate parameters beta for given experimental data (x, y)
    and basis functions f.

    Args:
    - f: List of function objects representing basis vectors
    - x: Array of independent variable values
    - y: Array of dependent variable values corresponding to x

    Returns:
    - beta: Array of parameters for the least squares regression
    """
    # Determine the number of data points
    n = len(x)

    # Determine the number of basis functions
    p = len(f)

    print("Number of data points:", n)
    print("Number of basis functions:", p)

    # Initialize the design matrix with zeros
    X = np.zeros((n, p))

    # Populate the design matrix by evaluating each basis function at each x value
    for i in range(n):
        for j in range(p):
            X[i, j] = f[j](x[i])

    print("Design matrix X:")
    print(X)

    # Perform least squares regression to estimate the parameters beta
    beta = np.linalg.lstsq(X, y, rcond=None)[0]

    print("Estimated parameters beta:")
    print(beta)

    return beta

# Example usage:
# Define basis functions
def f1(x):
    return x

def f2(x):
    return x ** 2

# Experimental data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.5, 3.5, 4.5, 5.5, 6.5])

# Perform least squares regression
beta = my_ls_params([f1, f2], x, y)
