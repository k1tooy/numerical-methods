#Write a function my_lin_regression(f, x, y) where f is a list containing function objects to 
#basis functions, and x and y are arrays containing noisy data. Assume that x and y are the same size.
#Let an estimation function for the data contained in x and y be defined as ˆ y(x)= β(1)·f1(x)+
#β(2) · f2(x) +···+β(n)·fn(x), where n is the length of f. Your function should compute beta
#according to the least squares regression formula.
#Test Case: Note that your solution may vary by a little bit, depending on the random numbers generated.

import numpy as np

def my_lin_regression(f, x, y):
    # Number of basis functions
    n = len(f)
    
    # Create the design matrix X
    X = np.zeros((len(x), n))
    for i in range(n):
        X[:, i] = f[i](x)
    
    # Compute beta using the least squares formula: beta = (X^T * X)^-1 * X^T * y
    beta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
    
    return beta

# Test Case
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 1000)
y = 3*np.sin(x) - 2*np.cos(x) + np.random.random(len(x))
f = [np.sin, np.cos]

beta = my_lin_regression(f, x, y)

plt.figure(figsize=(10, 8))
plt.plot(x, y, "b.", label="data")
plt.plot(x, beta[0]*f[0](x) + beta[1]*f[1](x), "r", label="regression")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Least Square Regression Example")
plt.legend()
plt.show()
