def my_lagrange(x, y, X):
    Y = 0
    for n in range(len(x)):
        product = y[n]
        for i in range(len(x)):
            if x[i] != x[n]:
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
