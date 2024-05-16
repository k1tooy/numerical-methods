#15.2 Suppose that for Example 15.1, the gas-processing plant
#decides to produce a third grade of product with the following
#characteristics:

import numpy as np
from scipy.optimize import linprog

# Coefficients of the objective function (negative because linprog does minimization)
c = [-45, -20, -250]

# Coefficients of the inequality constraints
A = [
    [20, 5, 0],
    [0.04, 0.12, 12],
    [1, 1, 5],
    [0, 0, 15]
]

# Right-hand side of the inequality constraints
b = [9500, 40, 550, 154]

# Bounds for each variable
x0_bounds = (0, None)
x1_bounds = (0, None)
x2_bounds = (0, None)

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds, x2_bounds], method='highs')

# Output the results
print(f"Status: {result.message}")
print(f"Optimal production of A: {result.x[0]} units")
print(f"Optimal production of B: {result.x[1]} units")
print(f"Optimal production of Supreme: {result.x[2]} units")
print(f"Maximum Profit: ${-result.fun}")
