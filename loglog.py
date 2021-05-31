#code for the log-log diagram for the following numerical integration methods:
#(i) Left Riemann sum, (ii) Right Riemann sum, (iii)Trapezoid, (iv)Simpson's

import numpy as np
import matplotlib.pyplot as plt
from integration_rules import rectangleL, rectangleR, trapezoid, simpson

f = lambda x: (np.exp(3*x)*np.sin(2*x))                       #function to integrate
a , b = 0, (np.pi)/4                                          #limits of integration
n = []
exact_solution = (1 / 13) * (3 * np.exp((3 * np.pi) / 4) + 2) #the exact solution of the given integral
error_T, error_S, error_L, error_R= [] , [], [], []


#for 10 iterations calculate the absolute error of each method
for i in range(0,10):
    n.append(4 ** i)
    approximate = rectangleL(f, a, b, n[i])
    error_L.append(abs(approximate - exact_solution))
    
    approximate = rectangleR(f, a, b, n[i])
    error_R.append(abs(approximate - exact_solution))
    
    approximate = trapezoid(f, a, b, n[i])
    error_T.append(abs(approximate - exact_solution)) 
    
    approximate = simpson(f, a, b, n[i]) 
    error_S.append(abs(approximate - exact_solution)) 
    


h = [((b - a) / j) for j in n]                              #step size

plt.figure()
plt.loglog(h,error_L,label = "Left Rectangle", color = "navy")
plt.loglog(h,error_R,label = "Right Rectangle", color = "r")
plt.loglog(h,error_T,label = "Trapezoid", color = "m")
plt.loglog(h,error_S,label = "Simpson's", color = "lime")
plt.xlabel("h")
plt.ylabel("error")
plt.title("Log-Log diagram")
plt.legend(loc = 4)
plt.show()