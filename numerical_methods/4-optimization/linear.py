import numpy as np


def find_sol(A, b):
    # Solve the system of equations
    return np.linalg.solve(A, b)

if __name__ == "__main__":
    # Define the coefficient matrix A and the constant vector b
    # A is the coeffecients of the variables and b is the constant
    A = np.array([[2, 3, 1], [4, 5, 6], [7, 8, 9]])
    b = np.array([1, 2, 3])
    sols = find_sol(A,b)
    # Print the solution
    print("The solution is:", sols)

