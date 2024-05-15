from scipy.optimize import linprog

# Coefficients of the objective function
c = [-3, -2]  # Since we are maximizing, we take the negative for minimization

# Coefficients of the inequality constraints
A = [
    [2, 1],
    [4, 3],
    [3, 2]
]

# Right-hand side of the inequality constraints
b = [20, 42, 30]

# Bounds for the variables
x0_bounds = (0, None)
x1_bounds = (0, None)

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

# Print the results
if result.success:
    print("Optimal value:", -result.fun)  # Multiply by -1 to get the maximum value
    print("x1:", result.x[0])
    print("x2:", result.x[1])
else:
    print("No solution found.")

