

import numpy as np
from scipy.optimize import minimize

# Constants
V = 50  # volume in cubic meters
C_excavation = 100  # cost per cubic meter of excavation
C_lining = 50  # cost per square meter of side lining
C_cover = 25  # cost per square meter of cover

# Volume of a cone V = (1/3) * pi * r^2 * h
# Surface area of the sides of the cone A_sides = pi * r * l (where l is the slant height)
# Surface area of the cover A_cover = pi * r^2

# Slant height l = sqrt(r^2 + h^2)

def cost_function(params):
    r, h = params
    l = np.sqrt(r**2 + h**2)
    volume = (1/3) * np.pi * r**2 * h
    if volume != V:
        return float('inf')  # Invalid volume

    cost_excavation = C_excavation * volume
    cost_lining = C_lining * np.pi * r * l
    cost_cover = C_cover * np.pi * r**2

    total_cost = cost_excavation + cost_lining + cost_cover
    return total_cost

# Constraint for the volume of the cone
def volume_constraint(params):
    r, h = params
    return (1/3) * np.pi * r**2 * h - V

# Constraint for side slope less than 45 degrees
def slope_constraint(params):
    r, h = params
    return np.arctan(h / r) - np.pi / 4

# Initial guess
initial_guess = [2, 5]

# Bounds for r and h (they must be positive)
bounds = [(0.01, None), (0.01, None)]

# Case (a): Unconstrained slope
result_a = minimize(cost_function, initial_guess, method='SLSQP', constraints={'type': 'eq', 'fun': volume_constraint}, bounds=bounds)
r_a, h_a = result_a.x
cost_a = result_a.fun

# Case (b): Slope less than 45 degrees
result_b = minimize(cost_function, initial_guess, method='SLSQP', constraints=[{'type': 'eq', 'fun': volume_constraint}, {'type': 'ineq', 'fun': slope_constraint}], bounds=bounds)
r_b, h_b = result_b.x
cost_b = result_b.fun

print(f"Case (a) - Unconstrained Slope:")
print(f"Radius: {r_a:.2f} m, Height: {h_a:.2f} m, Total Cost: ${cost_a:.2f}")

print(f"Case (b) - Slope less than 45°:")
print(f"Radius: {r_b:.2f} m, Height: {h_b:.2f} m, Total Cost: ${cost_b:.2f}")
