# Write a function my_func_fit (x,y) where x and y are column vectors of the same size containing
#experimental data, and the function returns alpha and beta are the parameters of the estimation
#function y(x) ˆ = αxβ.

#5                          3/5
import numpy as np

def my_func_fit(x, y):
    """
    Fit a power-law function y(x) = alpha * x**beta to experimental data.

    Args:
    - x: Column vector of independent variable values
    - y: Column vector of dependent variable values corresponding to x

    Returns:
    - alpha: Parameter alpha of the estimation function y(x) = alpha * x**beta
    - beta: Parameter beta of the estimation function y(x) = alpha * x**beta
    """
    # Compute the logarithms of x and y
    log_x = np.log(x)
    log_y = np.log(y)

    print("Logarithms of x:", log_x)
    print("Logarithms of y:", log_y)

    # Compute the mean of log_x and log_y
    mean_log_x = np.mean(log_x)
    mean_log_y = np.mean(log_y)

    print("Mean of log_x:", mean_log_x)
    print("Mean of log_y:", mean_log_y)

    # Compute the numerator and denominator for beta
    numerator = np.sum((log_x - mean_log_x) * (log_y - mean_log_y))
    denominator = np.sum((log_x - mean_log_x) ** 2)

    print("Numerator for beta:", numerator)
    print("Denominator for beta:", denominator)

    # Compute beta
    beta = numerator / denominator

    print("Computed beta:", beta)

    # Compute alpha using beta
    alpha = np.exp(mean_log_y - beta * mean_log_x)

    print("Computed alpha:", alpha)

    return alpha, beta

# Example usage:
# Experimental data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 8, 16, 32])

# Fit the power-law function
alpha, beta = my_func_fit(x, y)

print("Estimated parameters:")
print("Alpha:", alpha)
print("Beta:", beta)
