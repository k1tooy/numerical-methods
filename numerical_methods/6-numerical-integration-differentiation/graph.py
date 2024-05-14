import matplotlib.pyplot as plt
import numpy as np

def graph_function(func, x_range=(-10, 10), num_points=1000, title="Function Graph", xlabel="x", ylabel="y"):
    # Generate x values
    x_values = np.linspace(x_range[0], x_range[1], num_points)
    # Generate y values by applying the function to the x values
    y_values = func(x_values)
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, label=f"{func.__name__}(x)")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage:
def example_function(x):
    return np.sin(x)  # You can replace this with any mathematical function

graph_function(example_function, x_range=(-2 * np.pi, 2 * np.pi))

