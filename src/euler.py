import numpy as np

##implementation of the Euler's method to solve systems of differential equations##

def euler(F,x0,t0,tmax,dt):
    t = np.arange(t0,tmax,dt)
    x = np.zeros((len(t), len(x0)))
    x[0,:] = x0
    for n in range(len(t)-1):
        x[n+1,:] = x[n,:] + dt * F(t[n],x[n,:])
    return t, x


x0 = [ 20 , 1 ]  # initial conditions
t0 = 0
tmax = 200
dt = 0.1         # step size
F = lambda t,x: np.array([1.1*x[0] - 0.4*x[0]*x[1], 0.4*x[0] * x[1] - 0.1*x[1]])
t, x = euler(F,x0,t0,tmax,dt)
print(t)
print(x)
