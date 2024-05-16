#Determine the distance traveled for the following data:
#t, min 1 2 3.25 4.5 6 7 8 9 9.5 10
#v, m/s 5 6 5.5 7 8.5 8 6 7 7 5
#(a) Use the trapezoidal rule, 

import numpy as np

# Given data
t = np.array([1, 2, 3.25, 4.5, 6, 7, 8, 9, 9.5, 10])  # time in minutes
v = np.array([5, 6, 5.5, 7, 8.5, 8, 6, 7, 7, 5])  # velocity in m/s

# Initialize distance
distance_trap = 0

# Apply the trapezoidal rule
for i in range(len(t) - 1):
    distance_trap += (t[i+1] - t[i]) * (v[i] + v[i+1]) / 2

print(f'(a) Distance traveled using the trapezoidal rule is {distance_trap:.2f} meters')
