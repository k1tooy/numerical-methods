def my_rec_det(M:list):
    # If M is a 1x1 matrix, return its single element
    if len(M) == 1:
        return M[0][0]
    
    # Initialize determinant
    det = 0
    
    # Iterate over the elements of the first row
    for i in range(len(M)):
        # Calculate the minor of M by removing the first row and the i-th column
        minor = [row[:i] + row[i+1:] for row in M[1:]]
        
        # Calculate the determinant of the minor recursively
        minor_det = my_rec_det(minor)
        
        # Add the term to the determinant using Cramer's rule
        det += ((-1) ** i) * M[0][i] * minor_det
    
    return det

if __name__ == "__main__":
    # Define a square matrix
    M = [[1, 1, 2],
        [4, 3, 10],
        [7, 8, 9]]

    # Compute the determinant using Cramer's rule
    determinant = my_rec_det(M)
    print("Determinant:", determinant)

