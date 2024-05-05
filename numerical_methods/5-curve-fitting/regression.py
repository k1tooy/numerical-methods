import math


def exp_function(x, alpha, beta):
    return a * math.exp(beta * x)


def mean(values):
    return sum(values) / len(values)


def covariance(x, y):
    mean_x = mean(x)
    mean_y = mean(y)
    return sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x))) / len(x)


def variance(values):
    mean_val = mean(values)
    return sum((x - mean_val) ** 2 for x in values) / len(values)


def linear_regression(x, y):
    beta = covariance(x, y) / variance(x)
    alpha = mean(y) - beta * mean(x)
    return alpha, beta


def my_exp_regression(x, y):
    # Transform y values using natural logarithm
    y_ln = [math.log(val) for val in y]

    # Perform linear regression: Y = alpha + beta * X
    alpha, beta = linear_regression(x, y_ln)

    # Compute estimated parameters a and beta
    alpha = math.exp(alpha)
    beta = beta
    return alpha, beta


# Example usage:
x = [0, 1, 2, 3, 4]
y = [1, 2, 4, 8, 16]

alpha, beta = my_exp_regression(x, y)
print("Estimated parameters: alpha =", alpha, ", beta =", beta)
