import sympy as smp
import numpy as np
import matplotlib.pyplot as plt
import math

class Taylor_Series:
    def __init__(self, expr, x:float = 0, a:float=0, n:int=100) -> None:
        self.expr = expr
        self.x = x
        self.a = a
        self.n = n

    def get_approx(self, x=None, n=None) -> float:
        self.x = x if x is not None else self.x
        self.n = n if n is not None else self.n

        var = smp.symbols("x")
        result = 0
        for i in range(self.n):
            dx_expr = smp.diff(self.expr,var,i)
            dx_val = dx_expr.evalf(subs={var: self.a})
            numerator = (self.x - self.a)**i
            denominator = math.factorial(i)
            result += (numerator*dx_val)/denominator
        #result = str(result).rstrip('0').rstrip('.') if '.' in str(result) else str(result) #delete trailing zeros
        return float(result)

    # ignore inen na graph di inen nadara kay bonak ak
    def graph_series(self) -> None:
        test_x = np.arange(-5,5,0.2)
        fig, ax = plt.subplots()

        for i in range(self.n):
            approx_graphs = [self.get_approx(x=x_val,n=i) for x_val in test_x]
            ax.plot(test_x,approx_graphs, label=f"{i+1} terms approximation")

        ax.set_ylim([-5,5])
        ax.legend()
        plt.show()

    def expression(self):
        return self.expr
    
if __name__ == "__main__":
    x, y = smp.symbols("x y")
    example = Taylor_Series(smp.cos(x),x=6,n=100)
    approx = example.get_approx()
    print(f"Approximation of {example.expression()} at x = {example.x}: {approx}")
    
    # example2 = Taylor_Series(smp.exp(x),x=6,n=100)
    # approx2 = example2.get_approx()
    # print(f"Approximation of {example2.expression()}: {approx2}")
