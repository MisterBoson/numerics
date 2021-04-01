# Numerical Analysis Course - Physics Department Auth 
# Michael Chadolias  AEM: 14871
#
# Set 1st 
# Exercise 1c

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def f1(x):
    return 2*x+3*np.sin(4*x)-np.exp(x)
def fx(x):
    return 2+12*np.cos(4*x)-np.exp(x)
def fxx(x):
    return -48*np.sin(4*x)-np.exp(x)

#initial condition
x= [0.5,1.0]
iteration=[]
solution=[]

for i in range(0,10):
   x.append( x[i+1]- f1(x[i+1])/(f1(x[i+1])-f1(x[i]))*(x[i+1]-x[i]))
   iteration.append(i)
   solution.append(x[i+2])
   print('%.d %.16f'% (iteration[i], solution[i]))
   if x[-2]==x[-1]:
       break
   
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

#Confirm the error 
root= solution[N-1]
m= 1.618
k= (fxx(root)/(2*fx(root)))**(1/m)

error_n = np.array([solution[N-1]-solution[1]])
error_np1 = np.array([solution[N-1]-solution[2]])
for i in range (2,N-1):
    error_n = np.append(error_n, [solution[N-1]-solution[i]])
    error_np1 = np.append(error_np1, [solution[N-1]-solution[i+1]])

error_np1_predict = k*error_n**1.618

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
    
   
    
