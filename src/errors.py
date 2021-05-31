import sympy as sp
import numpy as np

## Small script to show the difference between the errors occuring in 
## the left Riemann's,Trapezoid's and Simpson's numerical integration rules. 

a , b = 0, np.pi/4                    #integration limits
n = 1000                              # number of equally spaced points
h = (b - a) / n
x = sp.Symbol('x')
f = sp.exp(3*x)*sp.sin(2*x) 

##error types for our methods using the nth derivatives
E_L = h * (b - a) * f.diff(x) * (1 / 2)
left_err = sp.lambdify(x, E_L)

E_T = - (1 / 12) * h**2 * (b - a) * f.diff(x,2)
trapezoid_err = sp.lambdify(x, E_T)

E_S = - (1 / 180) * (h / 2)**4 * (b - a) * f.diff(x,4)
simpson_err = sp.lambdify(x, E_S)

##calculate the upperbound errors for each method with constant h
print(f"Αριστερού παραλληλογράμμου: |E_L(h)| \u2264 {left_err(np.pi/4)}")
print(f"Τραπεζίου: |E_T(h)| \u2264 {abs(trapezoid_err(np.pi/4))}")
print(f"Simpson: |E_S(h)| \u2264 {simpson_err(np.pi/4)}")





