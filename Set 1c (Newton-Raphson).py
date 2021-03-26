# Numerical Analysis Course - Physics Department Auth 
# Michael Chadolias  AEM: 14871
#
# Set 1st 
# Exercise 1c


import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def f1(x):
    return 2*x+3*np.sin(4*x)-np.exp(x)

xpoints = np.linspace(-0.5,1,500)
fpoints = f1(xpoints)

plot1 = plt.plot(xpoints, fpoints)
plt.grid(True)
plt.show(plot1)

iteration = [0]
i=1
x=0.5
solution = [x]
print('%.d %.16f'% (iteration[0], solution[0]))
while True:
   x = x- f1(x)/(2+12*np.cos(4*x)-np.exp(x))
   iteration.append(i)
   solution.append(x)
   print('%.d %.16f'% (iteration[i], solution[i]))
   if solution[-1]==solution[-2]:
       break
   i=i+1
   
   N = len(solution)
error = solution[N-1]-solution
fig, ax = plt.subplots()
ax.plot(iteration, abs(error))
ax.set_yscale('log')
ax.set(xlabel='iteration', ylabel='error')
ax.grid()
plt.xlim(right=N-2)
tick_spacing = 1
ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
plt.show()