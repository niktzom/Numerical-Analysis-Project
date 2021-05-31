import numpy as np
import matplotlib.pyplot as plt
from euler import euler

## Code that generates the graphs of the population growth of rabbits and foxes 
## based on the Lotka-Volterra equations and Euler's method to solve the system.
## First one is plotting against time and the other against each other(phase state).

x0 = [ 20 , 1 ] # initial conditions
t0 = 0
tmax = 200
dt = 0.02
F = lambda t,x: np.array([1.1*x[0] - 0.4*x[0]*x[1], 0.4*x[0] * x[1] - 0.1*x[1]])
t, x = euler(F,x0,t0,tmax,dt)
# Plot the solutions against time
plt.figure(1)
plt.plot(t,x[:,:-1],"b-",label = "Rabbits")
plt.plot(t,x[:,-1],"r--",label = "Foxes")
plt.grid()
plt.title("Time Evolution of Foxes Population and Rabbits Population")
plt.xlabel("time")
plt.ylabel("No. of Rabbits and No. of Foxes")
plt.legend()

# Plot one solution against the other
# In this plot time is implicit (not one of the axes)
plt.figure(2)
plt.plot(x[:,:-1], x[:,-1], "k--")
plt.grid()
plt.title("Phase Plot")
plt.xlabel("Rabbit state")
plt.ylabel("Foxes state")
plt.show()