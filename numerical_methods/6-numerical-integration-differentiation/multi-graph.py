import matplotlib.pyplot as plt
import numpy as np

def graph_multiple_functions(funcs, labels, x_range=(-10, 10), num_points=1000, title="Multiple Functions Graph", xlabel="x", ylabel="y"):
    # Generate x values
    x_values = np.linspace(x_range[0], x_range[1], num_points)
    
    plt.figure(figsize=(10, 6))
    
    # Plot each function
    for func, label in zip(funcs, labels):
        y_values = func(x_values)
        plt.plot(x_values, y_values, label=label)
    
    # Add titles and labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()

# Example functions
def function1(x):
    return np.sin(x)

def function2(x):
    return np.cos(x)

def function3(x):
    return np.tan(x)

# Example usage
functions = [function1, function2, function3]
labels = ["sin(x)", "cos(x)", "tan(x)"]

graph_multiple_functions(functions, labels, x_range=(-2 * np.pi, 2 * np.pi))

