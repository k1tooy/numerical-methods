import numpy as np


def my_num_diff(f, a, b, n, option):
    h = (b - a) / (n - 1) # define value of h
    X = np.linspace(a, b, n) # initiate values

    if option == "forward":
        dy = np.zeros(n - 1) # initialize correct length of the array for the derivatives
        for i in range(n - 1): # cycle through the value
            dy[i] = (f(X[i+1]) - f(X[i])) / h # do forward method

    elif option == "backward":
        dy = np.zeros(n - 1)
        for i in range(1, n):
            dy[i - 1] = (f(X[i]) - f(X[i-1])) / h

    elif option == "central":
        dy = np.zeros(n - 2)
        for i in range(1, n - 1):
            dy[i - 1] = (f(X[i+1]) - f(X[i-1])) / (2 * h)
        X = X[0:-1] # match the length of X with dy

    return dy, X[0:-1]


if __name__ == "__main__":
    f = lambda  x: x**2

    # Compute numerical derivative using forward difference method
    dy, X = my_num_diff(f, 0, 1, 6, "forward")
    print(f"dy = {dy}, X = {X}")

    # Compute numerical derivative using backward difference method
    dy, X = my_num_diff(f, 0, 1, 6, "backward")
    print(f"dy = {dy}, X = {X}")

    # Compute numerical derivative using central difference method
    dy, X = my_num_diff(f, 0, 1, 6, "central")
    print(f"dy = {dy}, X = {X}")

