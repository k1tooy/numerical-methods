import numpy as np
from scipy.optimize import minimize

# Define the objective function
def objective(vars):
    x, y = vars
    return -(1.2 * x + 2 * y + y**3)

# Define the constraint function
def constraint(vars):
    x, y = vars
    return 2 - (2 * x + y)

# Initial guess for the variables
initial_guess = [0.5, 0.5]

# Define the bounds for the variables
bounds = [(0, None), (0, None)]

# Define the constraint in the format required by minimize
constraints = [{'type': 'ineq', 'fun': constraint}]

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
