import numpy as np
from scipy.optimize import minimize

# Define the objective function
def objective(vars):
    x, y = vars
    return -(15 * x + 15 * y)

# Define the constraint functions
def constraint1(vars):
    x, y = vars
    return 1 - (x**2 + y**2)

def constraint2(vars):
    x, y = vars
    return 2.1 - (x + 2 * y)

# Initial guess for the variables
initial_guess = [0.5, 0.5]

# Define the bounds for the variables
bounds = [(0, None), (0, None)]

# Define the constraints in the format required by minimize
constraints = [
    {'type': 'ineq', 'fun': constraint1},
    {'type': 'ineq', 'fun': constraint2}
]

# Perform the optimization
result = minimize(objective, initial_guess, method='SLSQP', bounds=bounds, constraints=constraints)

# Check if the optimization was successful
if result.success:
    x_opt, y_opt = result.x
    max_value = -result.fun  # Negate again to get the maximum value
    print(f"Optimal values: x = {x_opt}, y = {y_opt}")
    print(f"Maximum value of the objective function: {max_value}")
else:
    print("The optimization problem did not converge")
