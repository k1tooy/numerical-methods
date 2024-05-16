#13.16 Pressure measurements are taken at certain points behind an
#airfoil over time. These data best fi t the curve y 5 6 cos x 2 1.5 sin x
#from x 5 0 to 6 s. Use four iterations of the golden-search method
#to fi nd the minimum pressure. Set xl 5 2 and xu 5 4.

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

# Problem 13.16: Minimum pressure
def pressure(x):
    return 6 * np.cos(x) - 1.5 * np.sin(x)

a_16, b_16 = 2, 4
min_x_16 = golden_section_search(pressure, a_16, b_16)
min_pressure = pressure(min_x_16)
print(f'Problem 13.16: Minimum pressure at x = {min_x_16:.5f}, pressure = {min_pressure:.5f}')

