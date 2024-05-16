import numpy as np
import matplotlib.pyplot as plt

def my_num_diff_w_smoothing(x, y, n):
    """
    Compute the smoothed derivative of a given function using central difference.
    
    Parameters:
        x (numpy.ndarray): The x-values.
        y (numpy.ndarray): The y-values.
        n (int): The window size for smoothing.
    
    Returns:
        dy (numpy.ndarray): The derivative of the smoothed y-values.
        X (numpy.ndarray): The x-values corresponding to the derivative points.
    """
    if n < 1 or not isinstance(n, int):
        raise ValueError("n must be a strictly positive integer.")
    
    # Smooth the y-data
    y_smooth = np.array([np.mean(y[max(i-n, 0):min(i+n+1, len(y))]) for i in range(len(y))])
    
    # Compute the derivative using central difference
    dy = (y_smooth[2*n+1:] - y_smooth[:-2*n-1]) / (x[2*n+1:] - x[:-2*n-1])
    X = x[n:-n-1]  # Adjust x to ensure dimensions match those of dy

    return dy, X

# Now, retesting with corrected code
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x) + np.random.randn(len(x)) / 100
dy, X = my_num_diff_w_smoothing(x, y, 4)

# Plotting
plt.figure(figsize=(12, 12))
plt.subplot(211)
plt.plot(x, y)
plt.title("Noisy Sine function")
plt.xlabel("x")
plt.ylabel("y")

plt.subplot(212)
plt.plot(x, np.cos(x), "b", label="cosine")
plt.plot(x[:-1], (y[1:] - y[:-1]) / (x[1:] - x[:-1]), "g", label="unsmoothed forward diff")
plt.plot(X, dy, "r", label="smoothed")
plt.title("Analytic Derivative and Smoothed Derivative")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.tight_layout()
plt.show()

