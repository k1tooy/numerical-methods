import sympy as smp
import numpy as np
import math

class Taylor_Series:
    def __init__(self,expr,x:float = 0,a:float=0,n:int=10) -> None:
        self.expr = expr
        self.x = x
        self.a = a
        self.n = n

    def get_approx(self):
        var = smp.symbols("x")
        result = 0
        for i in range(self.n):
            dx_expr = smp.diff(self.expr,var,i)
            dx_val = dx_expr.evalf(subs={var: self.a})
            numerator = (self.x - self.a)**i
            denominator = math.factorial(i)
            result += (numerator*dx_val)/denominator
            print(f"{dx_expr}")
        result = str(result).rstrip('0').rstrip('.') if '.' in str(result) else str(result) #delete trailing zeros
        return result

    def expression(self):
        return self.expr

if __name__ == "__main__":
    x, y = smp.symbols("x y")
    example = Taylor_Series(smp.cos(x),x=1)
    approx = example.get_approx()
    print(approx)
