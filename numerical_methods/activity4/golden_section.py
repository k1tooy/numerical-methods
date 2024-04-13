def golden_section(func, a, b, tol) -> dict[float, float]:
    """
    Finds min/max of a function using golden section algorithm and returns the min/max x and f(x).

    arguments:
    func -- callable function to be used
    a -- lower bound
    b -- upper bound
    tol -- tolerance

    return: dict[x: float: f(x): float]
    """

    # get them bounds right
    if a >= b:int
        raise ValueError("a must be smaller than b")

    phi = (1+ 5**0.5)/2
    d = (phi - 1)*(b - a)

    # find new values
    x1 = a + d
    x2 = b - d

    # for comparison with respect to the tolerance
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
    # we enter the negative of the function since we are maximizing (reflecting across x-axis)
    f = lambda x: -(x**2 - 6*x + 15)

    print(golden_section(f, 1, 4, 0.01))
