# Numerical Methods Activity 1 Moreno
from collections.abc import Callable
import math
import sys
import matplotlib.pyplot as plt
import numpy as np

# Maclaurin Series for sinx and returns a float
def func_sin(x: float, n_terms: int) -> float:
    result: float = 0
    for n in range(n_terms): # Summing up the results until the nth term
        coefficient = (-1) ** n # the supposedly f^n
        term = x ** (2 * n + 1) / math.factorial(2 * n + 1)
        result += coefficient * term
    return result

# Maclaurin Series for e^(x^2)
def my_double_exp(x: float, n_terms: int) -> float:
    result: float = 0
    for i in range(n_terms): # Summing up the results until the nth term
        numerator = x ** (2*i)
        denominator = math.factorial(i)
        result += numerator / denominator
    return result

# Plot the Series
def graph(func: Callable[[float, int], float], n: int):
    test_x = np.arange(-5,5,0.1)
    fig, ax = plt.subplots()

    for i in range(n):
        approx_graphs = [func(x,i) for x in test_x]
        ax.plot(test_x,approx_graphs, label=f"{i+1} terms approximation")

    ax.set_ylim([-5,5])
    ax.legend()
    plt.show()

if __name__ == "__main__":
    # 1st argument is the x value
    # 2nd argument is the n terms
    # 3rd argument is either 0 for sin function and 1 for exp function

    choice = int(sys.argv[3])

    if choice == 0:
        approximation = func_sin(float(sys.argv[1]), int(sys.argv[2]))
        print(f"Linear Approximation: sin({sys.argv[1]}) = {approximation}")
        print(f"sin(x)/x = {approximation/float(sys.argv[1])}")

        graph(func_sin, int(sys.argv[2]))

    if choice == 1:
        exp = my_double_exp(float(sys.argv[1]),int(sys.argv[2]))
        print(f"Linear Approximation: e^({sys.argv[1]}^2) = {exp}")
