import numpy as np

def velocity(x, y, h):
    #using central difference
    n = len(x)
    dy = np.zeros(n - 2)
    for i in range(1, n - 1):
        dy[i - 1] = (y[i+1] - y[i-1]) / (2 * h)
    x = x[1:-1]  # match the length of X with dy

    return dy, x

def acceleration(x, y, h):
    #using central difference
    n = len(x)
    d_2y = np.zeros(n - 2)
    for i in range(1, n - 1):
        d_2y[i - 1] = (y[i+1] - 2*y[i] + y[i-1]) / (h**2)
    x = x[1:-1]  # match the length of X with dy

    return d_2y, x
if __name__ == "__main__":
    x = [0, 25, 50, 75, 100, 125]
    y = [0, 32, 58, 78, 92, 100]
    h = 25

    velocity, time = velocity(x, y, h)
    print(f"time(s): {time}, velocity(km/s): {velocity}")
    
    accel, time = acceleration(x, y, h)
    print(f"time(s): {time}, acceleration(km/s^2): {accel}")
