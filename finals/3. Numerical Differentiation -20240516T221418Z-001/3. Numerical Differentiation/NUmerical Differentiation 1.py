#Write a function my_der_calc(f, a, b, N, option) with the output as [df,X], where f is a function 
#object, a and b are scalars such that a < b,N is an integer bigger than 10, and option is the
#string "forward", "backward",or"central".Letx be an array starting at a, ending at b, containing N 
#evenly spaced elements, and let y be the array f(x). The output argument, df, should be the
#numerical derivatives computed for x and y according to the method defined by the input argument,
#option. The output argument X should be an array the same size as df, containing the points in x for
#which df is valid. Specifically, the forward difference method “loses” the last point, the backward
#difference method loses the first point, and the central difference method loses the first and last points.

import numpy as np

def my_der_calc(f, a, b, N, option):
    """
    Calculate the numerical derivatives of the function f over the interval [a, b] using a specified method.
    
    Parameters:
        f (callable): The function to differentiate. Must be a function of a single variable.
        a (float): The start of the interval over which to calculate derivatives.
        b (float): The end of the interval over which to calculate derivatives.
        N (int): The number of points in the interval [a, b]. Must be greater than 10.
        option (str): The method to use for differentiation ('forward', 'backward', 'central').
    
    Returns:
        df (numpy.ndarray): Array of calculated derivatives.
        X (numpy.ndarray): Array of x values at which derivatives are calculated.
    """
    if N <= 10:
        raise ValueError("N must be greater than 10")
    if not (a < b):
        raise ValueError("a must be less than b")

    # Create an array of N evenly spaced points from a to b
    x = np.linspace(a, b, N)
    # Calculate the function values at each point
    y = f(x)
    # Calculate the step size
    h = (b - a) / (N - 1)

    if option == "forward":
        # Forward difference method (excludes the last point)
        df = (y[1:] - y[:-1]) / h
        X = x[:-1]
    elif option == "backward":
        # Backward difference method (excludes the first point)
        df = (y[1:] - y[:-1]) / h
        X = x[1:]
    elif option == "central":
        # Central difference method (excludes the first and last points)
        df = (y[2:] - y[:-2]) / (2 * h)
        X = x[1:-1]
    else:
        raise ValueError("Option must be 'forward', 'backward', or 'central'")

    return df, X

import matplotlib.pyplot as plt

def sample_function(x):
    return x**2 + 2*x + 1  # Example function f(x) = x^2 + 2x + 1

a = 0
b = 10
N = 100

# Compute derivatives using all methods
df_forward, X_forward = my_der_calc(sample_function, a, b, N, "forward")
df_backward, X_backward = my_der_calc(sample_function, a, b, N, "backward")
df_central, X_central = my_der_calc(sample_function, a, b, N, "central")

# Plotting results to visualize
plt.figure(figsize=(10, 6))
plt.plot(X_forward, df_forward, label='Forward Difference')
plt.plot(X_backward, df_backward, label='Backward Difference')
plt.plot(X_central, df_central, label='Central Difference')
plt.legend()
plt.title('Numerical Differentiation')
plt.xlabel('x')
plt.ylabel('df/dx')
plt.grid(True)
plt.show()
