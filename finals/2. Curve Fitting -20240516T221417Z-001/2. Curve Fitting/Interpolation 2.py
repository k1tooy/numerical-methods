import numpy as np
from scipy.interpolate import CubicSpline

def my_D_cubic_spline(x, y, X, D):
    # Create a cubic spline with custom endpoint conditions
    spline = CubicSpline(x, y, bc_type=((1, D), (1, D)))

    # Evaluate the spline at points X
    Y = spline(X)

    return Y

# Test case
x = [0, 1, 2, 3, 4]
y = [0, 0, 1, 0, 0]
X = np.linspace(0, 4, 101)

# Solution: Y = 0.54017857
Y = my_D_cubic_spline(x, y, 1.5, 1)

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
plt.subplot(221)
plt.plot(x, y, "ro", X, my_D_cubic_spline(x, y, X, 0), "b")
plt.subplot(222)
plt.plot(x, y, "ro", X, my_D_cubic_spline(x, y, X, 1), "b")
plt.subplot(223)
plt.plot(x, y, "ro", X, my_D_cubic_spline(x, y, X, -1), "b")
plt.subplot(224)
plt.plot(x, y, "ro", X, my_D_cubic_spline(x, y, X, 4), "b")
plt.tight_layout()
plt.show()
