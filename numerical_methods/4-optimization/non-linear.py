import numpy as np
from scipy.optimize import minimize

# Objective function to maximize (negated for maximization)


def objective(x):
    return -(15*x[0] + 15*x[1])

# Constraints


def constraint1(x):
    return x[0]**2 + x[1]**2 - 1  # x^2 + y^2 <= 1


def constraint2(x):
    return x[0] + 2*x[1] - 2.1  # x + 2y <= 2.1


# Initial guess as numpy array
initial_guess = np.array([0, 0])

# Define bounds for variables
bounds = ((0, None), (0, None))  # Non-negativity constraints

# Define constraints
constraints = [{'type': 'ineq', 'fun': constraint1},
               {'type': 'ineq', 'fun': constraint2}]

# Perform optimization
result = minimize(objective, initial_guess,
                  bounds=bounds, constraints=constraints)

# Print results
print("Optimal solution:", result.x)
print("Maximum value:", -result.fun)  # Negate the result for maximization
