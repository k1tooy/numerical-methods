def my_exp_regression(x, y):
    sum_of_x = sum(x)
    sum_of_y = sum(y)
    sum_of_xy = sum(xy(x,y))
    n = min(len(x), len(y))
    
    m_numerator = n*sum_of_xy - sum_of_x*sum_of_y
    m_denominator = n*sum(square_of_x(x)) - (sum_of_x)**2
    m = m_numerator/m_denominator

    b = (sum_of_y - m*sum_of_x)/n
    return f"y = {m}x + {b}"

def xy(x,y):
    result = []
    for i in range(min(len(x), len(y))):
        result.append(x[i]*y[i])
    return result

def square_of_x(x):
    return [i**2 for i in x]

if __name__ == "__main__":
    x = [1,2,3,4,5,6,7,8]
    y = [2,4,6,8,10,12,14,16]
    print(my_exp_regression(x,y))
