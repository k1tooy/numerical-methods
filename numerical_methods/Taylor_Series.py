import sympy as smp
from sympy.abc import x
import numpy as np
import math
import matplotlib.pyplot as plt

def get_taylor_approx(expr, x: float=1, a:float=0, n: int= 1):
    var = smp.symbols("x")
    result = 0
    for i in range(n):
        dx_expr = smp.diff(expr,var,i)
        dx_val = dx_expr.evalf(subs={var: a},chop=True)
        numerator = (x-a)**i
        denominator = math.factorial(i)
        result += (numerator*dx_val)/denominator
    result = str(result).rstrip('0').rstrip('.') if '.' in str(result) else str(result) #delete trailing zeros
    return result

if __name__ == "__main__":
    x, y = smp.symbols("x y")
    print(get_taylor_approx(x**3,x=5,n=10))
