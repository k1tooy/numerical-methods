import sympy as smp
from sympy.abc import x
import numpy as np
import math
import matplotlib.pyplot as plt

def get_taylor_approx(expr, x: float, n: int= 1):
    var = smp.symbols("x")
    dx_expr = smp.diff(expr,var,n)
    result = dx_expr.evalf(subs={var: x})
    return result

if __name__ == "__main__":
    x, y = smp.symbols("x y")
    print(get_taylor_approx(x**3,1,2))
