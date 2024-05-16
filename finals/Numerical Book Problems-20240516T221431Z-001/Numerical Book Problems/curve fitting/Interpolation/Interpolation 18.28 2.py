import numpy as np

# Data
temperature = np.array([0, 8, 16, 24, 32, 40])
oxygen = np.array([14.621, 11.843, 9.870, 8.418, 7.305, 6.413])

# Newton's interpolating polynomial
def newton_interpolation(x, xp, yp):
    n = len(xp)
    divided_diff = np.zeros((n, n))
    divided_diff[:, 0] = yp

    for j in range(1, n):
        for i in range(n - j):
            divided_diff[i, j] = (divided_diff[i + 1, j - 1] - divided_diff[i, j - 1]) / (xp[i + j] - xp[i])

    result = divided_diff[0, 0]
    product = 1.0
    for j in range(1, n):
        product *= (x - xp[j - 1])
        result += divided_diff[0, j] * product

    return result

estimated_oxygen_newton = newton_interpolation(27, temperature, oxygen)
print(f"Estimated oxygen concentration at 27°C using Newton's interpolating polynomial: {estimated_oxygen_newton:.3f} mg/L")
