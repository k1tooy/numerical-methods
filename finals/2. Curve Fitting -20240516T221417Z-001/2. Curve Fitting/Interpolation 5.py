def my_nearest_neighbor(x, y, X):
    # Initialize an empty array to store interpolated values
    Y = []

    # Loop through each point in X
    for xi in X:
        # Find the index of the nearest neighbor in x
        idx = min(range(len(x)), key=lambda i: abs(x[i] - xi))
        
        # Append the corresponding y value to the result array
        Y.append(y[idx])
    
    return Y

# Test case
x = [0, 1, 2, 3, 4]
y = [0, 2, 4, 6, 8]
X = [0.5, 1.5, 2.5, 3.5]

Y = my_nearest_neighbor(x, y, X)
print(Y)  # Output: [0, 2, 4, 6]
