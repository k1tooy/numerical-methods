import math
import matplotlib.pyplot as plt
import numpy as np

def func_cos(x, n):
    cos_approx = 0
    for i in range(n):
        coef = (-1)**i
        num = x**(2*i)
        denom = math.factorial(2*i)
        cos_approx += ( coef ) * ( (num)/(denom) )
    
    return cos_approx

def graph(func, n):
    angles = np.arange(-2*np.pi,2*np.pi,0.1)
    p_cos = np.cos(angles)

    fig, ax = plt.subplots()

    for i in range(n):
        t_cos = [func(angle,i) for angle in angles]
        ax.plot(angles,t_cos, label=f"{i} terms approximation")

    ax.plot(angles,p_cos)
    ax.set_ylim([-5,5])
    ax.legend()
    plt.show()

if __name__ == "__main__":
    graph(func_cos, 3)
