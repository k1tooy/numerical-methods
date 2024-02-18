from collections.abc import Callable
import math
import sys
import matplotlib.pyplot as plt
import numpy as np

# Maclaurin Series for sinx
def func_sin(x: float, n_terms: int) -> float:
    result: float = 0
    for n in range(n_terms):
        coefficient = (-1) ** n
        term = x ** (2 * n + 1) / math.factorial(2 * n + 1)
        result += coefficient * term
    return result

# Maclaurin Series for e^(x^2)
def my_double_exp(x: float, n_terms: int) -> float:
    result: float = 0
    for i in range(n_terms):
        numerator = x ** (2*i)
        denominator = math.factorial(i)
        result += numerator / denominator
    return result

#Plot the Series
def graph(func: Callable[[float, int], float], n: int):
    test_x = np.arange(-5,5,0.1)
    fig, ax = plt.subplots()

    for i in range(n):
        approx_graphs = [func(x,i) for x in test_x]
        ax.plot(test_x,approx_graphs, label=f"{i+1} terms approximation")

    ax.set_ylim([-5,5])
    ax.legend()
    plt.show()
    
#Taylor Series Formula
def taylor_series_expansion(f, a, x):
    pass

def taylor_series_approx(f,a,x):
    pass

if __name__ == "__main__":
    choice = int(sys.argv[3]) #Passes the third argument as choice on what function to use
    if choice == 0:
        approximation = func_sin(float(sys.argv[1]), int(sys.argv[2]))
        print(f"Linear Approximation: sin({sys.argv[1]}) = {approximation}")
        print(f"sin(x)/x = {approximation/float(sys.argv[1])}")

        graph(func_sin, int(sys.argv[2]))

    if choice == 1:
        exp = my_double_exp(float(sys.argv[1]),int(sys.argv[2]))
        print(f"Linear Approximation: e^({sys.argv[1]}^2) = {exp}")
