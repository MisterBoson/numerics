# Numerical Analysis Course - Physics Department Auth 
# Michael Chadolias  AEM: 14871
#
# Set 1st 
# Exercise 3a

import numpy as np
import matplotlib.pyplot as plt

#functions and derivatives
def f1(x,y):
    return 2*x-np.exp(x)+3-y
def g1(x,y):
    return 0.5*x-2*x**3-y
def fx(x):
    return 2-np.exp(x)
def gx(x):
    return 0.5-6*x**2
fy,gy=-1,-1


xpoints = np.linspace(-1,2,300)
ypoints = np.linspace(-1,2,300)
fpoints = f1(xpoints,ypoints)
gpoints= g1(xpoints,ypoints)


plot1 = plt.plot(ypoints, gpoints, ypoints,fpoints)
plt.grid(True)
plt.show(plot1)


#initial conditions
x,y= 1,-1
x_sol, y_sol=[],[]
iteration=[]

for i in range(1,15):
    xnew =  x - (f1(x,y)*gy-g1(x,y)*fy)/(fx(x)*gy-gx(x)*fy)
    ynew =  y - (g1(x,y)*fx(x)-f1(x,y)*gx(x))/(fx(x)*gy-gx(x)*fy)
    x = xnew
    y = ynew
    x_sol.append(xnew)
    y_sol.append(ynew)
    iteration.append(i)
    print('%.16f'% x, '%.16f'% y)

