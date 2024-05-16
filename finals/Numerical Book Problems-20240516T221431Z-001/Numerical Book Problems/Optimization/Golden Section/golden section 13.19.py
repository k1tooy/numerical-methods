#13.19 An object with a mass of 100 kg is projected upward from the
#surface of the earth at a velocity of 50 m/s. If the object is subject to
#linear drag (c 5 15 kg/s), use the golden-section search to determine
#the maximum height the object attains. Hint: recall Sec. PT4.1.2.

import numpy as np

# Golden-section search parameters
phi = (1 + np.sqrt(5)) / 2  # Golden ratio

def golden_section_search(f, a, b, tol=1e-5, max_iter=100):
    c = b - (b - a) / phi
    d = a + (b - a) / phi
    for _ in range(max_iter):
        if abs(b - a) < tol:
            break
        if f(c) < f(d):
            b = d
        else:
            a = c
        c = b - (b - a) / phi
        d = a + (b - a) / phi
    return (b + a) / 2

# Problem 13.19: Maximum height
# Placeholder height function (replace with actual function if provided)
def height(t):
    v0 = 50  # initial velocity in m/s
    g = 9.81  # gravity in m/s^2
    c = 15  # drag coefficient in kg/s
    m = 100  # mass in kg
    return (m/c) * (v0 + (m/c) * g) * (1 - np.exp(-c * t / m)) - g * t

a_19, b_19 = 0, 10  # Interval should be determined based on physical constraints
max_t_19 = golden_section_search(height, a_19, b_19)
max_height = height(max_t_19)
print(f'Problem 13.19: Maximum height at t = {max_t_19:.5f}, height = {max_height:.5f}')
