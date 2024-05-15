import math

def least_square_regression(x, y):
    m = slope(x,y)

def slope(x,y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum([x[i] * y[i] for i in range(len(x))])
    sum_x_squared = sum([x[i]**2 for i in range(len(x))])

    return (n*sum_xy - sum_x*sum_y)/(n*sum_x_squared - sum_x**2)

def intercept(x,y,slope):
    sum_y = sum(y)
    sum_x = sum(x)
    n = len(x)
    return (sum_y - slope*sum_x)/n

def exp_function(x, a, beta):
    return a * math.exp(beta * x)

if __name__ == "__main__":
    pass
