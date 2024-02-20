import sympy as smp
from sympy import *
from sympy.abc import x
import numpy as np
import math
import matplotlib.pyplot as plt

def get_taylor_approx(expr, x: float=0, a:float=0, n: int=10):
    var = smp.symbols("x")
    result = 0
    for i in range(n):
        dx_expr = smp.diff(expr,var,i)
        dx_val = dx_expr.evalf(subs={var: a})
        numerator = (x-a)**i
        denominator = math.factorial(i)
        result += (numerator*dx_val)/denominator
        print(f"{dx_expr}*{numerator}/{denominator}={result}")
    result = str(result).rstrip('0').rstrip('.') if '.' in str(result) else str(result) #delete trailing zeros
    return result

if __name__ == "__main__":
    x, y = smp.symbols("x y")
    print(get_taylor_approx(cos(x),x=5, n=20))
