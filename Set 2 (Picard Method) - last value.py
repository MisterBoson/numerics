# Numerical Analysis Course - Physics Department Auth 
# Michael Chadolias  AEM: 14871
#
# Set 1st 
# Exercise 1b

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def f1(x):
    return 2*x+3*np.sin(4*x)-np.exp(x)

def z1(x):
    return np.log(2*x+3*np.sin(4*x))
"""
def g1x(x):
    return (np.exp(x)-6*np.cos(4*x))/2
"""
xpoints = np.linspace(1.5,2,30)
fpoints = f1(xpoints)
zpoints= z1(xpoints)


#last root is arround 1.9

plot1 = plt.plot(xpoints, fpoints)
plt.grid(True)
plt.show(plot1)

#x=1.75
x=1.9 
diff= 10**(-12)
sol=[]
iteration=[]

for i in range(0,500):
    xnew=z1(x)
    sol.append(xnew)
    iteration.append(i)
    x=xnew
    print('%.d %.16f'% (iteration[i], sol[i]))
    if len(iteration)>=2 and (sol[-1]-sol[-2]<diff):
        break

N = len(sol)
error = sol[N-1]-sol
fig, ax = plt.subplots()
ax.plot(iteration, abs(error))
ax.set_yscale('log')
ax.set(xlabel='iteration', ylabel='error')
ax.grid()
plt.ylim(bottom=abs(error[-2]))
plt.show()