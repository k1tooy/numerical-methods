#The following data are provided for the velocity of an object as a function of time,
# t, s 0 4 8 12 16 20 24 28 32 36
 #v, m/s034.7 61.8 82.8 99.2112.0121.9129.7135.7140.4
 #(a) Using the best numerical method available, how far does the object travel from t 5 0 to 28 s?
 #(b) Using the best numerical method available, what is the object’s acceleration at t 5 28 s?
 #(c) Using the best numerical method available, what is the object’s acceleration at t 5 0 s?

import numpy as np

# Given data
t = np.array([0, 4, 8, 12, 16, 20, 24, 28, 32, 36])  # time in seconds
v = np.array([0, 34.7, 61.8, 82.8, 99.2, 112.0, 121.9, 129.7, 135.7, 140.4])  # velocity in m/s

# Part (a): Calculate the distance traveled from t = 0 to t = 28 s
# Using the trapezoidal rule
def trapezoidal_integration(x, y):
    return np.trapz(y, x)

distance_0_to_28 = trapezoidal_integration(t[:8], v[:8])  # Only considering t = 0 to 28 s

# Part (b): Calculate the object's acceleration at t = 28 s
# Using central difference method for acceleration (second derivative)
def central_difference(x, y, idx):
    if idx == 0:  # Forward difference for the first point
        return (y[idx + 2] - 2 * y[idx + 1] + y[idx]) / (x[idx + 1] - x[idx])**2
    elif idx == len(y) - 1:  # Backward difference for the last point
        return (y[idx] - 2 * y[idx - 1] + y[idx - 2]) / (x[idx] - x[idx - 1])**2
    else:  # Central difference for interior points
        return (y[idx + 1] - 2 * y[idx] + y[idx - 1]) / ((x[idx + 1] - x[idx - 1]) / 2)**2

acceleration_28 = central_difference(t, v, 7)  # t = 28 s corresponds to index 7

# Part (c): Calculate the object's acceleration at t = 0 s
acceleration_0 = central_difference(t, v, 0)  # t = 0 s corresponds to index 0

# Print the results
print("Part (a): Distance traveled from t = 0 to 28 s is {:.2f} meters".format(distance_0_to_28))
print("Part (b): Acceleration at t = 28 s is {:.2f} m/s^2".format(acceleration_28))
print("Part (c): Acceleration at t = 0 s is {:.2f} m/s^2".format(acceleration_0))
