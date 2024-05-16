#Assume you have a function in the form y(x) ˆ = αeβx and data for x and y, and that you want to
#perform least squares regression to find α and β. Clearly, the previous set of basis functions (linear)
#would be inappropriate to describe y(x) ˆ ; however, if we take the log of both sides, we get log(y(x)) ˆ =
#log(α) + βx. Now, we see that if y(x) ˜ = log(y(x)) ˆ and α˜ = log(α), then y(x) ˜ = ˜α + βx. Thus, we can
#perform a least squares regression on the linearized expression to find y(x), ˜ α˜, and β, and then recover
#α by using the expression α = eα˜ .
#For the example below, we will generate data using α = 0.1 and β = 0.3.

#2

# Import the NumPy library for numerical computations
import numpy as np

# Import the pyplot module from the Matplotlib library for creating visualizations
import matplotlib.pyplot as plt

# Import the LinearRegression class from the linear_model module of the scikit-learn library for performing linear regression
from sklearn.linear_model import LinearRegression

# Set the parameters for the function y(x) = alpha * e^(beta * x)
alpha = 0.1
beta = 0.3

# Generate x values as an array of 101 evenly spaced numbers between 0 and 1
x = np.linspace(0, 1, 101)

# Generate y values based on the function y(x) = alpha * e^(beta * x)
y = alpha * np.exp(beta * x)

# Add some noise to y
y += np.random.normal(scale=0.01, size=y.shape)

# Take the natural logarithm of y
y_log = np.log(y)

# Reshape x into a 2D array with one column and as many rows as necessary for scikit-learn
x = x.reshape(-1, 1)

# Create an instance of the LinearRegression class
model = LinearRegression()

# Fit the linear regression model to the data points (x, y_log)
model.fit(x, y_log)

# Print the coefficients of the linear regression model
print(f"α~ = {model.intercept_}, β = {model.coef_[0]}")

# Recover alpha by taking the exponential of the intercept
alpha_recovered = np.exp(model.intercept_)

# Print the recovered alpha
print(f"α = {alpha_recovered}")

# Create a scatter plot of the original data points
plt.scatter(x, y, color='blue', label='Data points')

# Use the fitted model to predict the y-values for the given x-values
y_pred = alpha_recovered * np.exp(model.coef_[0] * x)

# Plot the least squares regression line
plt.plot(x, y_pred, color='red', label='Least squares regression')

# Add a legend to the plot
plt.legend()

# Display the plot
plt.show()


