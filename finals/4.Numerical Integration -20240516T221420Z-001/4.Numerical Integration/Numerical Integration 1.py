#Write a function my_poly_int(x,y) where x and y are one-dimensional arrays of the same size,
 #and the elements of x are unique and in ascending order. The function my_poly_int should (1)
 #compute the Lagrange polynomial going through all the points defined by x and y; and (2) return
 #an approximation to the area under the curve defined by x and y, I, defined as the analytic integral
 #of the Lagrange interpolating polynomial.

import numpy as np
from scipy.integrate import quad

def lagrange_basis(x, x_points, i):
    """
    Compute the Lagrange basis polynomial L_i(x) for the given x and x_points.
    """
    L = 1
    x_i = x_points[i]
    for j in range(len(x_points)):
        if j != i:
            x_j = x_points[j]
            L *= (x - x_j) / (x_i - x_j)
    return L

def lagrange_polynomial(x, x_points, y_points):
    """
    Compute the Lagrange interpolating polynomial P(x) for the given x, x_points, and y_points.
    """
    P = 0
    for i in range(len(x_points)):
        P += y_points[i] * lagrange_basis(x, x_points, i)
    return P

def integral_lagrange_polynomial(x_points, y_points):
    """
    Compute the analytical integral of the Lagrange interpolating polynomial over the interval [x_min, x_max].
    """
    x_min = x_points[0]
    x_max = x_points[-1]
    
    integral, _ = quad(lambda x: lagrange_polynomial(x, x_points, y_points), x_min, x_max)
    return integral

def my_poly_int(x, y):
    """
    Compute the Lagrange polynomial for points defined by x and y, and return the integral under the curve.
    """
    if len(x) != len(y):
        raise ValueError("x and y must have the same length")
    
    # Ensure x is in ascending order and elements are unique
    if not np.all(np.diff(x) > 0):
        raise ValueError("x must be in ascending order and have unique elements")
    
    # Compute the integral of the Lagrange interpolating polynomial
    integral = integral_lagrange_polynomial(x, y)
    
    return integral

# Example usage
x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])
I = my_poly_int(x, y)
print(f"Integral: {I}")
