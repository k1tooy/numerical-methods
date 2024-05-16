from scipy.optimize import linprog

# Objective function coefficients (note that linprog does minimization by default, so we negate the coefficients)
c = [-6, -8]

# Coefficients of the inequality constraints (Ax <= b)
A = [
    [5, 2],
    [6, 6],
    [2, 4]
]

# Right-hand side values of the inequality constraints
b = [40, 60, 32]

# Bounds for the variables x and y
x_bounds = (0, None)
y_bounds = (0, None)

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Check if the optimization was successful
if result.success:
    x_opt, y_opt = result.x
    max_value = -result.fun  # Negate again to get the maximum value
    print(f"Optimal values: x = {x_opt}, y = {y_opt}")
    print(f"Maximum value of the objective function: {max_value}")
else:
    print("The optimization problem did not converge")
