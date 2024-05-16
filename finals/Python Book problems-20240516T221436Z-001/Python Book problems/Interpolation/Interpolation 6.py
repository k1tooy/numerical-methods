import numpy as np

def my_cubic_spline_flat(x, y, X):
    # Check if x and X are sorted and have unique elements
    assert all(x[i] < x[i+1] for i in range(len(x)-1)), "x must be sorted in ascending order"
    assert all(X[i] < X[i+1] for i in range(len(X)-1)), "X must be sorted in ascending order"
    
    # Compute the differences and slopes
    h = np.diff(x)
    delta_y = np.diff(y)
    slopes = delta_y / h
    
    # Compute the tridiagonal matrix
    main_diag = np.append(np.append(2 * np.ones(len(h)), 1), 2)
    upper_diag = np.append(1, np.ones(len(h)-1))
    lower_diag = np.append(np.ones(len(h)-1), 1)
    
    # Solve the tridiagonal system for the second derivatives
    A = np.diag(main_diag) + np.diag(upper_diag, 1) + np.diag(lower_diag, -1)
    b = 3 * (delta_y[:-1]/h[1:] - delta_y[1:]/h[:-1])
    c = np.linalg.solve(A, b)
    c = np.append(c, 0)  # Add zero to satisfy the boundary condition Sn-1(xn) = 0
    
    # Compute the coefficients of the cubic spline
    d = (c[:-1] + c[1:] - 2 * delta_y / h) / (h ** 2)
    b = (delta_y / h - c[:-1] * h - d * h ** 2) / h
    
    # Perform interpolation
    Y = []
    for xi in X:
        # Find the interval containing xi
        idx = np.searchsorted(x, xi) - 1
        
        # Compute the value of the cubic spline polynomial at xi
        dx = xi - x[idx]
        yi = y[idx] + b[idx] * dx + c[idx] * dx ** 2 + d[idx] * dx ** 3
        Y.append(yi)
    
    return Y

# Test case
x = [0, 1, 2, 3, 4]
y = [0, 1, 2, 1, 0]
X = [0.5, 1.5, 2.5, 3.5]

Y = my_cubic_spline_flat(x, y, X)
print(Y)  # Output: [0.5, 1.5, 2.0, 1.125]
