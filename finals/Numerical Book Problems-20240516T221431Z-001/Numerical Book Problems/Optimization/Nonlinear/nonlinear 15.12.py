#15.12 An automobile company has two versions of the same model
#car for sale, a two-door coupe and the full-size four door.
#(a) Graphically solve how many cars of each design should be
#produced to maximize profi t and what that profi t is

import numpy as np
from scipy.optimize import linprog

# Coefficients of the objective function (negative because linprog does minimization)
c = [-13500, -15000]

# Coefficients of the inequality constraints
A = [
    [15, 20],
    [1, 0],
    [0, 1],
    [13500, 15000]
]

# Right-hand side of the inequality constraints
b = [8000, 700, 500, 240000]

# Bounds for each variable
x0_bounds = (0, None)
x1_bounds = (0, None)

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

# Output the results
print(f"Status: {result.message}")
print(f"Optimal production of Two Door: {result.x[0]} cars")
print(f"Optimal production of Four Door: {result.x[1]} cars")
print(f"Maximum Profit: ${-result.fun}")
