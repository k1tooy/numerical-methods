import sympy as sp

def my_newton(f, df, x0, tol, R=None, E=None):
    # Define symbols
    x = sp.Symbol('x')

    # Initialize lists for roots and errors if not provided
    if R is None:
        R = [x0]  # Initial estimate of the root
    if E is None:
        E = [abs(f.subs(x, x0))]  # Absolute value of f(x0)

    # Base case: If the absolute value of f(x0) is less than tol, return R and E
    if E[-1] < tol:
        return R, E

    # Recursive case: Perform Newton-Raphson method
    else:
        # Calculate the next estimate of the root using the Newton-Raphson method
        x_next = R[-1] - f.subs(x, R[-1]) / df.subs(x, R[-1])
        
        # Update the estimate of the root and the absolute value of f at the new estimate
        R.append(x_next.evalf())
        E.append(abs(f.subs(x, x_next.evalf())))
        
        # Recursively call the function with updated lists R and E
        return my_newton(f, df, x0, tol, R, E)
    # Define the function and its derivative
    x = sp.Symbol('x')
    f = x**2 - 2  # Example function: f(x) = x^2 - 2
    df = sp.diff(f, x)  # Derivative of f(x)

    roots, errors = my_newton(f, df, 1, 1e-5)
    print("Roots:", roots)
    print("Errors:", errors)
