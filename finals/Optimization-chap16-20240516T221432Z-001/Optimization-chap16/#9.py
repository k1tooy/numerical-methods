#Optimization parabolic interpolation

import numpy as np
from numpy import sin

def parabolic_interpolation(f, x0, x1, x2, tol=1e-6, max_iter=100):
    """
    Perform parabolic interpolation to find the minimum of a function.

    Args:
    - f: Function to be minimized
    - x0, x1, x2: Initial points for interpolation (x0 < x1 < x2)
    - tol: Tolerance for convergence
    - max_iter: Maximum number of iterations

    Returns:
    - x_min: Approximation of the minimum
    """
    # Check if points are distinct
    if x0 == x1 or x0 == x2 or x1 == x2:
        raise ValueError("The three points must be distinct.")
    
    for _ in range(max_iter):
        # Fit a parabola through the three points
        f0, f1, f2 = f(x0), f(x1), f(x2)
        denom = (x0 - x1) * (x0 - x2) * (x1 - x2)
        if denom == 0:
            raise ValueError("Denominator is zero. The three points must be distinct.")
        A = (x2 * (f1 - f0) - x1 * (f2 - f0) + x0 * (f2 - f1)) / denom
        B = (x2**2 * (f0 - f1) + x1**2 * (f2 - f0) + x0**2 * (f1 - f2)) / denom
        C = (x1 * x2 * (x1 - x2) * f0 + x2 * x0 * (x2 - x0) * f1 + x0 * x1 * (x0 - x1) * f2) / denom

        # Calculate the vertex of the parabola
        x_min = -B / (2 * A)

        # Calculate the function value at the minimum
        f_min = f(x_min)

        # Check convergence
        if abs(x_min - x1) < tol:
            break

        # Update points for next iteration
        if x_min > x1:
            if f_min < f1:
                x0, f0 = x1, f1
                x1, f1 = x_min, f_min
            else:
                x2, f2 = x_min, f_min
        else:
            if f_min < f1:
                x2, f2 = x1, f1
                x1, f1 = x_min, f_min
            else:
                x0, f0 = x_min, f_min

    return x_min

# Example usage
def f(x):
    return (x**2/10)-2*sin(x)

x0, x1, x2 = 0, 1, 4  # Initial points (adjusted to ensure distinctness)
x_min = parabolic_interpolation(f, x0, x1, x2)
print("Approximation of the minimum:", x_min)
print("Minimum value of the function:", f(x_min))
