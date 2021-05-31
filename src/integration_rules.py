# Functions that implement the following integration rules(composite forms):
# (i)Left rectangle(left Riemann sum)
# (ii)Right rectangle(right Riemann sum)
# (iii)Trapezoid rule
# (iv)Simpson's rule
# We also run a small test calculating the integral of x^3 from 1 to 2 for each method.

import numpy as np


def rectangleL(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a,b,n+1)
    x_left = x[:-1]
    return np.sum(f(x_left) * h)


print(f"Left rectangle rule ={rectangleL(lambda x: (np.exp(3*x)*np.sin(2*x)), 0, np.pi/4, 100)}")

def rectangleR(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a,b,n+1)
    x_right = x[1:]
    return np.sum(f(x_right) * h)
    

print(f"Right rectangle rule = {rectangleR(lambda x: (np.exp(3*x)*np.sin(2*x)), 0, np.pi/4, 100)}")



def trapezoid(f, a, b, n):
    h = float(b - a) / n
    s = f(a)
    for i in range(1,n):
        x = a + (h * i)
        s += 2 * f(x)
    s += f(b)
    return h * (s/2)


print(f"Trapezoid rule = {trapezoid(lambda x: (np.exp(3*x)*np.sin(2*x)), 0, np.pi/4, 10000)}")


def simpson(f, a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)

    for i in range(1, n, 2):
        s += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        s += 2 * f(a + i * h)

    return s * h / 3


print(f"Simpson rule = {simpson(lambda x: (np.exp(3*x)*np.sin(2*x)), 0, np.pi/4, 10**6)}")





