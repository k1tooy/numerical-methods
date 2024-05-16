import numpy as np
from scipy.optimize import minimize

# Define the objective function
def objective(vars):
    x, y = vars
    return (x - 3)**2 + (y - 3)**2

# Define the constraint function
def constraint(vars):
    x, y = vars
    return x + 12 * y - 54

# Initial guess for the variables
initial_guess = [0, 0]

# Define the bounds for the variables
bounds = [(None, None), (None, None)]

# Define the constraint in the format required by minimize
constraints = [{'type': 'ineq', 'fun': constraint}]

# Perform the optimization
result = minimize(objective, initial_guess, method='SLSQP', bounds=bounds, constraints=constraints)

# Check if the optimization was successful
if result.success:
    x_opt, y_opt = result.x
    min_value = result.fun
    print(f"Optimal values: x = {x_opt}, y = {y_opt}")
    print(f"Minimum value of the objective function: {min_value}")
else:
    print("The optimization problem did not converge")
