def golden_section(func, a, b, tol) -> dict:
    # get them bounds right
    if a >= b:
        raise ValueError("a must be smaller than b")

    phi = (1+ 5**0.5)/2
    d = (phi - 1)*(b - a)

    # find new values
    x1 = a + d
    x2 = b - d

    # for comparison with tolerance
    c = abs(x1 - x2)

    # approximation of the maximum
    avg = (x1 + x2)/2

    # base case
    if c < tol:
        return {avg: func(avg)}

    # recursive case
    else:
        if func(x1) > func(x2):
            return golden_section(func, x2, b, tol)
        elif func(x1) < func(x2):
            return golden_section(func ,a, x1, tol)

if __name__ == "__main__":
    # example function 
    f = lambda x: -(x**2 - 6*x + 15)
    print(golden_section(f, 1, 4, 0.01))
