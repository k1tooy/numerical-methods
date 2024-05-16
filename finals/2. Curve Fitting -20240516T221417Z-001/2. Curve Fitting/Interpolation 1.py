#Write a function my_interp_plotter(x, y, X, option) where x and y are arrays containing
#experimental data points, and X is an array that contains the coordinates for which an interpolation
#is desired. The input argument option should be a string, either “linear,” “spline,” or “nearest.”
#Your function should produce a plot of the data points (x,y) marked as red circles. The points
#(X,Y), where X is the input and Y is the interpolation at the points contained in X defined by the
#input argument specified by option. The points (X,Y) should be connected by a blue line. Be sure
#to include the title, axis labels, and a legend. Hint: You should use interp1d from SciPy, and
#checkout the kind option.

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def my_interp_plotter(x, y, X, option):
    # Interpolate based on the specified option
    if option == "linear":
        interp_func = interp1d(x, y, kind='linear')
    elif option == "spline":
        interp_func = interp1d(x, y, kind='cubic')
    elif option == "nearest":
        interp_func = interp1d(x, y, kind='nearest')
    else:
        raise ValueError("Invalid option. Please choose 'linear', 'spline', or 'nearest'.")

    # Interpolate Y values at points X
    Y = interp_func(X)

    # Plot the original data points
    plt.plot(x, y, 'ro', label='Experimental Data')

    # Plot the interpolated points
    plt.plot(X, Y, 'b-', label='Interpolation (' + option + ')')

    # Add title and labels
    plt.title('Interpolation Plot (' + option + ' method)')
    plt.xlabel('x')
    plt.ylabel('y')

    # Add legend
    plt.legend()

    # Show the plot
    plt.show()

# Test case
x = np.array([0, .1, .15, .35, .6, .7, .95, 1])
y = np.array([1, 0.8187, 0.7408, 0.4966, 0.3012, 0.2466, 0.1496, 0.1353])
X = np.linspace(0, 1, 101)
my_interp_plotter(x, y, X, "spline")
