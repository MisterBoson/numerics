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
plt.ylim(bottom=abs(error[-2]))
plt.show()

#confirm the convergence of the error with the theoretical prediction
root = solution[N-1]
k = (48.0*np.sin(4.0*root)+np.exp(root))/(2.0*(12.0*np.cos(4.0*root)+2.0-np.exp(root)))
                           
error_n = np.array([solution[N-1]-solution[1]])
error_np1 = np.array([solution[N-1]-solution[2]])
for i in range (2,N-1):
    error_n = np.append(error_n, [solution[N-1]-solution[i]])
    error_np1 = np.append(error_np1, [solution[N-1]-solution[i+1]])

error_np1_predict = k*error_n**2

NE = len(error_n)
fig, ax = plt.subplots()
ax.plot(abs(error_n), abs(error_np1_predict),label="Theoretical Prediction")
ax.plot(abs(error_n), abs(error_np1),label="Experimental Prediction")
ax.legend()
ax.set(xlabel='error_n', ylabel='error_n+1')
ax.set_xscale('log')
ax.set_yscale('log')

#plt.ylim(bottom=abs(error_np1[NE-1]))
#plt.xlim(left=abs(error_np1[NE-2]))

ax.grid()
plt.show()