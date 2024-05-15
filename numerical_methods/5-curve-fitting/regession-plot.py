import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate or provide data points
np.random.seed(0)  # For reproducibility
x = np.linspace(0, 10, 50)
y = 2.5 * x + np.random.normal(size=x.size)

# Step 2: Calculate the least squares regression line
# Compute the coefficients (slope and intercept) of the regression line
A = np.vstack([x, np.ones(len(x))]).T
slope, intercept = np.linalg.lstsq(A, y, rcond=None)[0]

# Step 3: Plot the data points and the regression line
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Data points')
plt.plot(x, slope * x + intercept, color='red', label=f'Least squares line: y = {slope:.2f}x + {intercept:.2f}')

# Add titles and labels
plt.title('Least Squares Regression')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

