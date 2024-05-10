import math


def exp_function(x, a, beta):
    return a * math.exp(beta * x)


def mean(values):
    return sum(values) / len(values)


def covariance(x, y):
    n = len(x)
    xy = [x[i] * y[i] for i in range(n)]
    return sum(xy) - (sum(x)*sum(y))/n


def variance(values):
    x_squared = [x**2 for x in values]
    return sum(x_squared) - sum(values)**2/len(values)


def least_square_regression(x, y):
    beta = covariance(x, y) / variance(x)
    alpha = mean(y) - beta * mean(x)
    return alpha, beta


def my_exp_regression(x, y):
    # Transform y values using natural logarithm
    y_ln = [math.log(val) for val in y]

    # Perform linear regression: Y = alpha + beta * X
    alpha, beta = least_square_regression(x, y_ln)

    # Compute estimated parameters a and beta
    a = math.exp(alpha)
    beta = beta
    return a, beta


# Example usage:
x = [1, 2, 3, 4, 5]
y = [3, 5, 7, 9, 11]

a, beta = my_exp_regression(x, y)
print("Estimated parameters: a =", a, ", beta =", beta)
