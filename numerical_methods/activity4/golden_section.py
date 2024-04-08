def golden_section(func, a, b, tol) -> dict:
    if a >= b:
        raise ValueError("a must be smaller than b")

    phi = (1+ 5**0.5)/2
    d = (phi - 1)*(b - a)
    x1 = a + d
    x2 = b - d
    c = abs(x1 - x2)
    avg = (x1 + x2)/2

    # base case
    if c < tol:
        return {avg: func(avg)}

    # recursive case
    else:
        if func(x1) > func(x2):
            return golden_section(func, a, x2, tol)
        elif func(x1) < func(x2):
            return golden_section(func ,x1, b, tol)

if __name__ == "__main__":
    # make f(x) be -f(x) to find maximum
    f = lambda x: x**2 - 6*x + 15

    print(golden_section(f, 1, 4, 0.01))
