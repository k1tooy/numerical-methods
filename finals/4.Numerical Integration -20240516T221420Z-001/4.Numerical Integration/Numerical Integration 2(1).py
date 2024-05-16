

import numpy as np

def my_num_calc(f, a, b, n, option):
    """
    Compute the numerical integral of function f from a to b using n points and the specified method.
    
    Parameters:
    f (function): The integrand function.
    a (float): The start of the interval.
    b (float): The end of the interval.
    n (int): The number of points (must be odd for Simpson's rule).
    option (str): The integration method ("rect", "trap", "simp").
    
    Returns:
    float: The numerical integral of f from a to b.
    """
    if n % 2 == 0:
        raise ValueError("n must be odd for Simpson's rule.")
    
    x = np.linspace(a, b, n)
    h = (b - a) / (n - 1)
    
    if option == "rect":
        I = np.sum(f(x[1:])) * h
    
    elif option == "trap":
        I = (f(a) + f(b)) / 2.0
        I += np.sum(f(x[1:-1]))
        I *= h
    
    elif option == "simp":
        I = f(a) + f(b)
        I += 4 * np.sum(f(x[1:-1:2]))
        I += 2 * np.sum(f(x[2:-2:2]))
        I *= h / 3.0
    
    else:
        raise ValueError("Unknown option. Use 'rect', 'trap', or 'simp'.")
    
    return I

# Test cases
f1 = lambda x: x**2
print(my_num_calc(f1, 0, 1, 3, "rect"))  # Output: 0.625
print(my_num_calc(f1, 0, 1, 3, "trap"))  # Output: 0.375
print(my_num_calc(f1, 0, 1, 3, "simp"))  # Output: 0.3333333333333333

f2 = lambda x: np.exp(x**2)
print(my_num_calc(f2, -1, 1, 101, "simp"))  # Output: 2.9253035883926493
print(my_num_calc(f2, -1, 1, 10001, "simp"))  # Output: 2.925303491814364
print(my_num_calc(f2, -1, 1, 100001, "simp"))  # Output: 2.9253034918143634
