#Og is the leader of the surprisingly mathematically advanced, though technologically run-of-the-mill, Calm Waters cave
#man tribe. He must decide on the number of stone clubs and stone axes to be produced for the upcoming battle against the neighboring
#Peaceful Sunset tribe. Experience has taught him that each club is 
#good for, on the average, 0.45 kills and 0.65 maims, while each axe 
#produces 0.70 kills and 0.35 maims. Production of a club requires 
#5.1 lb of stone and 2.1 man-hours of labor while an axe requires 3.2 lb 
#of stone and 4.3 man-hours of labor. Og’s tribe has 240 lb of stone 
#available for weapons production, and a total of 200 man-hours of 
#labor available before the expected time of this battle (that Og is sure 
#will end war for all time). Og values a kill as worth two maims in 
#quantifying the damage infl icted on the enemy, and he wishes to 
#produce that mix of weapons that will maximize damage.
 #(a) Formulate this as a linear programming problem. Make sure to define your decision variables.
 #(b) Represent this problem graphically, making sure to identify all the feasible corner points and the infeasible corner points.
 #(c) Solve the problem graphically.
 #(d) Solve the problem using the computer.

import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

# Coefficients of the objective function
c = [-0.775, -0.875]  # We negate because linprog does minimization

# Coefficients of the inequality constraints
A = [
    [5.1, 3.2],  # Stone constraint
    [2.1, 4.3]   # Labor constraint
]

# Right-hand side of the inequality constraints
b = [240, 200]

# Bounds for x and y (both should be non-negative)
x_bounds = (0, None)
y_bounds = (0, None)

# Solve the problem using linprog
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Results
x_opt, y_opt = result.x
max_damage = -result.fun  # Negate to get the maximized value

print(f"Optimal number of stone clubs (x): {x_opt:.2f}")
print(f"Optimal number of stone axes (y): {y_opt:.2f}")
print(f"Maximum damage: {max_damage:.2f}")

# Step (c): Graphical solution
# Define the constraints for plotting
x_vals = np.linspace(0, 50, 400)
stone_constraint = (240 - 5.1 * x_vals) / 3.2
labor_constraint = (200 - 2.1 * x_vals) / 4.3

# Plotting the feasible region
plt.figure(figsize=(10, 8))
plt.plot(x_vals, stone_constraint, label='Stone Constraint (5.1x + 3.2y <= 240)')
plt.plot(x_vals, labor_constraint, label='Labor Constraint (2.1x + 4.3y <= 200)')

# Filling the feasible region
plt.fill_between(x_vals, 0, np.minimum(stone_constraint, labor_constraint), alpha=0.3)

# Adding optimal point
plt.plot(x_opt, y_opt, 'ro', label='Optimal Solution')

# Labels and legend
plt.xlabel('Number of Stone Clubs (x)')
plt.ylabel('Number of Stone Axes (y)')
plt.title('Feasible Region for Weapon Production')
plt.xlim(0, 50)
plt.ylim(0, 50)
plt.legend()
plt.grid(True)
plt.show()
