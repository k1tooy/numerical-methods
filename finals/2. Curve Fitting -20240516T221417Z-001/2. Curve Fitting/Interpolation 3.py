def my_lin_interp(x, y, X):
    # Initialize an empty array to store interpolated values
    Y = []

    # Loop through each point in X
    for xi in X:
        # Find the two points in x that surround xi
        idx = 0
        while x[idx] < xi:
            idx += 1
        
        # Perform linear interpolation between the two surrounding points
        x0, x1 = x[idx - 1], x[idx]
        y0, y1 = y[idx - 1], y[idx]
        
        # Calculate the interpolated value for xi
        yi = y0 + (y1 - y0) * (xi - x0) / (x1 - x0)
        
        # Append the interpolated value to the result array
        Y.append(yi)
    
    return Y

# Test case
x = [0, 1, 2, 3, 4]
y = [0, 2, 4, 6, 8]
X = [0.5, 1.5, 2.5, 3.5]

Y = my_lin_interp(x, y, X)
print(Y)  # Output: [1.0, 3.0, 5.0, 7.0]
