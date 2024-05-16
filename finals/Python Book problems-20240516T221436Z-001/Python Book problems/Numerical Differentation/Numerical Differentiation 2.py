#Write a function my_num_diff(f,a,b,n,option) with the output as [df,X], where f is a function
 #object. The function my_num_diff should compute the derivative of f numerically for n evenly
 #spaced points starting at a and ending at b, according to the method defined by option. The input
 #argument option is one of the following strings: "forward", "backward", and "central".Note
 #that for the forward and backward method, the output argument, dy, should be a 1D array of length
 #n−1,andforthe central difference method dy it should be a 1D array of length n−2. The function
 #should also output a vector X that is the same size as dy and denotes the x-values for which dy is
 #valid.

import numpy as np

def my_num_diff(f, a, b, n, option):
    """
    Compute the derivative of a function numerically for n evenly spaced points starting at a and ending at b.
    
    Parameters:
        f (callable): The function to differentiate. It should be a function of one variable.
        a (float): The start of the interval over which to compute the derivative.
        b (float): The end of the interval.
        n (int): The number of evenly spaced points in the interval.
        option (str): The method for numerical differentiation ("forward", "backward", "central").
    
    Returns:
        dy (numpy.ndarray): The array of numerical derivatives.
        X (numpy.ndarray): The array of x-values at which the derivatives are computed.
    """
    # Generate n evenly spaced points from a to b
    x = np.linspace(a, b, n)
    # Compute function values at these points
    y = f(x)
    # Compute the step size
    h = (b - a) / (n - 1)
    
    if option == "forward":
        # Forward difference method (uses n-1 points)
        dy = (y[1:] - y[:-1]) / h
        X = x[:-1]
    elif option == "backward":
        # Backward difference method (uses n-1 points)
        dy = (y[1:] - y[:-1]) / h
        X = x[1:]
    elif option == "central":
        # Central difference method (uses n-2 points)
        dy = (y[2:] - y[:-2]) / (2 * h)
        X = x[1:-1]
    else:
        raise ValueError("Invalid option. Must be 'forward', 'backward', or 'central'")

    return dy, X

# Example Usage:
if __name__ == "__main__":
    import matplotlib.pyplot as plt

    x = np.linspace(0, np.pi, 1000)
f = lambda x: np.sin(np.exp(x))
dy10, X10 = my_num_diff(f, 0, np.pi, 10, "central")
dy20, X20 = my_num_diff(f, 0, np.pi, 20, "central")
dy100, X100 = my_num_diff(f, 0, np.pi, 100, "central")

# Plotting the results
plt.figure(figsize=(12, 8))
plt.plot(x, np.cos(np.exp(x)) * np.exp(x), label="Analytic")  # Correct analytic derivative
plt.plot(X10, dy10, label="10 points")
plt.plot(X20, dy20, label="20 points")
plt.plot(X100, dy100, label="100 points")
plt.legend()
plt.title("Analytic and Numerical Derivatives of Sine")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
