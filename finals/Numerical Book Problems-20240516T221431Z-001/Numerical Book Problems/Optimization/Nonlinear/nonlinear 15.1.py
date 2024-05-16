#15.1 A company makes two types of products, A and B. These
#products are produced during a 40-hr work week and then shipped
#out at the end of the week. They require 20 and 5 kg of raw material
#per kg of product, respectively, and the company has access to 9500 kg
#of raw material per week. Only one product can be created at a time
#with production times for each of 0.04 and 0.12 hr, respectively.
#The plant can only store 550 kg of total product per week. Finally,
#the company makes profi ts of $45 and $20 on each unit of A and B,
#respectively. Each unit of product is equivalent to a kg.
#(a) Set up the linear programming problem to maximize profi t.
#(b) Solve the linear programming problem graphically.
#(c) Solve the linear programming problem with the simplex method.
#(d) Solve the problem with a software package.
#(e) Evaluate which of the following options will raise profi ts the
#most: increasing raw material, storage, or production time.
#15.2 Suppose that for Example 15.1, the gas-processing plant

import numpy as np
from scipy.optimize import linprog

# Coefficients of the objective function (negative because linprog does minimization)
c = [-45, -20]

# Coefficients of the inequality constraints
A = [
    [20, 5],
    [0.04, 0.12],
    [1, 1]
]

# Right-hand side of the inequality constraints
b = [9500, 40, 550]

# Bounds for each variable
x0_bounds = (0, None)
x1_bounds = (0, None)

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

# Output the results
print(f"Status: {result.message}")
print(f"Optimal production of A: {result.x[0]} units")
print(f"Optimal production of B: {result.x[1]} units")
print(f"Maximum Profit: ${-result.fun}")
