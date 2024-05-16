import numpy as np

def my_cubic_spline(x, y, X):
    n = len(x)
    m = len(X)
    Y = np.zeros(m)

    # Find the index of the interval for each X[i]
    indices = np.searchsorted(x, X)

    for i in range(m):
        index = indices[i]

        if index == 0:
            index = 1
        elif index == n:
            index = n - 1

        h = x[index] - x[index - 1]
        a = (x[index] - X[i]) / h
        b = (X[i] - x[index - 1]) / h

        Y[i] = a * y[index - 1] + b * y[index] + ((a**3 - a) * y[index - 1] + (b**3 - b) * y[index]) * h**2 / 6

    return Y

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 1, 3, 6, 2])
X = np.linspace(1, 5, 100)

Y = my_cubic_spline(x, y, X)

plt.figure(figsize=(10, 8))
plt.plot(x, y, "bo", label="Data")
plt.plot(X, Y, "r-", label="Cubic Spline Interpolation")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Cubic Spline Interpolation Example")
plt.legend()
plt.show()