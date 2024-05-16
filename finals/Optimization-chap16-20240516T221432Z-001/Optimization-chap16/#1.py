# Consider the artificial data created by x = np.linspace(0, 1, 101) and y=1+x
#+ x * np.random.random(len(x)). Do a least squares regression with an estimation function
#defined by yˆ = α1x + α2. Plot the data points along with the least squares regression. Note that
#we expect α1 = 1.5 and α2 = 1.0 based on this data. Due to the random noise we added into the
#data, your results maybe slightly different.

#1
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Create artificial data
x = np.linspace(0, 1, 101)
y = 1 + x + x * np.random.random(len(x))

# Reshape x to 2D array for sklearn
x = x.reshape(-1, 1)

# Perform least squares regression
model = LinearRegression()
model.fit(x, y)

# Print the coefficients
print(f"α1 = {model.coef_[0]}, α2 = {model.intercept_}")

# Plot the data points
plt.scatter(x, y, color='blue', label='Data points')

# Plot the least squares regression
y_pred = model.predict(x)
plt.plot(x, y_pred, color='red', label='Least squares regression')

plt.legend()
plt.show()
