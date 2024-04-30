# Tigamni la na it gamit hit curve fitting kay pagbiling hin function na maangay hit im set of points.
# Bagat reverse engineering hit function bagat tibalik tim step
# Di ba han algebra may function ka magbiling kan points pero didi kay baliktad given kan points tagi ak function sugad

def my_lagrange(x, y, X) -> float:
    """
    Curve fitting using lagrange algorithm

    arguments:
        x -- x-values of points
        y -- y-values of points
        X -- x-value of the intermediate point to calculate

    returns:
        Y:float -- the estimated y-value
    """

    Y = 0
    # amo na inen dinhi an formula gud
    for n in range(len(x)):
        product = y[n]
        for i in range(len(x)):
            # inen dinhi amo inen an bagat dako na pi ba
            if x[i] != x[n]:  # handle ZeroDivisionError
                # make a polynomial function that is zero except at x-value in concern
                numerator = X - x[i]
                denominator = x[n] - x[i]
                product *= (numerator/denominator)
        Y += product
    return Y


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    Y = my_lagrange(x, y, 9)
    print(Y)  # should return float 18
