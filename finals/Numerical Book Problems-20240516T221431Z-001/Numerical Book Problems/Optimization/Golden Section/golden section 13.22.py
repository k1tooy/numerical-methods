#13.22 Use the golden-section search to determine the length of the
#shortest ladder that reaches from the ground over the fence to touch the
#building’s wall (Fig. P13.22). Test it for the case where h 5 d 5 4 m.

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

# Problem 13.22: Shortest ladder length
h = 4
def ladder_length(d):
    return np.sqrt(d**2 + h**2) + d

a_22, b_22 = 0.1, 10  # d must be positive, upper bound can be set reasonably
shortest_d_22 = golden_section_search(ladder_length, a_22, b_22)
shortest_length = ladder_length(shortest_d_22)
print(f'Problem 13.22: Shortest ladder length with d = {shortest_d_22:.5f}, length = {shortest_length:.5f}')
