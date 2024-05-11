from scipy.optimize import minimize
import numpy as np

# Objective function
def f(x):
    return -1 * (15*x[0] + 15*x[1])  # Negative sign for maximization


if __name__ == "__main__":
    #Define Constraints
    cons = {'type': 'ineq',
            'fun' : lambda x: np.array([1 - x[0]**2 - x[1]**2,  # x^2 + y^2 <= 1
                                        2.1 - x[0] - 2*x[1]])}  # x + 2y <= 2.1



    # Define the bounds
    bnds = [(0, None), (0, None)]  # x >= 0, y >= 0

    #Initial Guess
    x0 = np.array([0, 0])

    solution = minimize(f, x0, method='SLSQP',constraints=cons, bounds=bnds)

    print("x: ", solution.x[0])
    print("y: ", solution.x[1])
    print("f(x,y): ", -1 * f(solution.x))  # Multiply by -1 because we minimized -f(x,y)

