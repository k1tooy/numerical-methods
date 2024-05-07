import numpy as np
from scipy.optimize import minimize


def exponential_function(x, alpha, beta):
    return alpha * np.exp(beta * x)


def objective(params, x, y):
    alpha, beta = params
    y_pred = exponential_function(x, alpha, beta)
    return np.sum((y - y_pred)**2)


def my_exp_regression(x, y):
    initial_guess = [1, 1]  # Initial guess for alpha and beta
    result = minimize(objective, initial_guess, args=(x, y))
    alpha_opt, beta_opt = result.x
    return alpha_opt, beta_opt


# Example usage:
x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 2, 4, 8, 16])

alpha, beta = my_exp_regression(x, y)
print("Estimated parameters: alpha =", alpha, ", beta =", beta)
