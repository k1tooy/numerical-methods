import sympy as smp

def my_bisection(f, a, b, tol, R=None, E=None)-> list:

 # R and E cannot be empty. It is initialized here.
    if R is None:
        R = [(a + b) / 2]  # Initial estimate of the root
    if E is None:
        E = [abs(f.evalf(subs={x:((a + b) / 2)}))]  # Absolute value of f(R[0])

    # Base case: If the absolute value of f(R[i]) is less than tol, return lists R and E
    if E[-1] < tol:
        return R, E
    
    # Recursive case: Perform bisection method
    else:
        c = (a + b) / 2
        if f.evalf(subs={x: a}) * f.evalf(subs={x: c}) < 0:
            R.append((a + c) / 2)
            E.append(abs(f.evalf(subs={x: (a + c) / 2})))
            return my_bisection(f, a, c, tol, R, E)
        else:
            R.append((c + b) / 2)
            E.append(abs(f.evalf(subs={x: (c + b) / 2})))
            return my_bisection(f, c, b, tol, R, E)

if __name__ == "__main__":
    x = smp.symbols("x")
    root, error = my_bisection(x**(3) - 4,1,3,1e-6)

    print(f"Roots:{root}")
    print(f"Errors:{error}")
