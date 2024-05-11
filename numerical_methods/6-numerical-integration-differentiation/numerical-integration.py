import numpy as np

def my_int_calc(f, f0, a, b, N, option):
    x = np.linspace(a, b, N) # array of 0 to 1 with 100 steps
    h = (b - a) / N #define value of h
    
    if option == "rect": # rectangular method
        I = h * sum(f(x))
    elif option == "trap": # trapezoidal method
        I = h * (0.5 * f(a) + 0.5 * f(b) + sum(f(x[1:-1])))
    elif option == "simp": # simpson's rule
        I = h / 3 * (f(a) + f(b) + 4 * sum(f(x[1:-1:2])) + 2 * sum(f(x[2:-1:2])))
    else: #error handling if option is invalid
        raise ValueError("Invalid option. Choose 'rect', 'trap', or 'simp'.")
    
    return f0 + I

if __name__ == "__main__":
    # Example using trapezoidal method:
    result = my_int_calc(lambda x: x**2, 0, 0, 1, 100, "trap")
    print(result)

