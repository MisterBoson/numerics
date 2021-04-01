# Numerical Analysis Course - Physics Department Auth 
# Michael Chadolias  AEM: 14871
#
# Set 1st 
# Exercise 1b - Bolzano Method

import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return 2*x+3*np.sin(4*x)-np.exp(x)

#main
diff= 10**(-12)
iteration= [1]
a ,b ,index= 0.5, 1.0 , 1
distance= [a,b]
fun=[] #function
sol=[] 
mesos= np.average(distance)

while True:
    if (f1(distance[0])*f1(mesos))<0:
        distance[-1]= mesos
        fun.append(f1(mesos))
        sol.append(mesos)
       # print('%.d %.16f'% (iteration[-1], func(mesos)))
        mesos= np.average(distance)
    else:
        distance[0]= mesos
        fun.append(f1(mesos))
        sol.append(mesos)
      #  print('%.d %.16f'% (iteration[-1], func(mesos)))
        mesos= np.average(distance)
    if len(iteration)>=2 and (np.abs(sol[-1]-sol[-2])<diff):
        print("For error", diff ,"the iteration must reach:",'%.d %.16f'%(iteration[-1], sol[-1]))
        break
    iteration.append(index)
    index= index+1    

N = len(sol)
error = sol[N-1]-sol
fig, ax = plt.subplots()
ax.plot(iteration, abs(error))
ax.set_yscale('log')
ax.set(xlabel='iteration', ylabel='error')
ax.grid()
plt.ylim(bottom=abs(error[-2]))
plt.show()

#Confirm the plot 
root= sol[-1]
error_n = np.array([sol[N-1]-sol[0]])
error_np1 = np.array([sol[N-1]-sol[1]])

for i in range (1,N-1):
    error_n = np.append(error_n, [sol[N-1]-sol[i]])
    error_np1 = np.append(error_np1, [sol[N-1]-sol[i+1]])
    
error_np1_predict= error_n/2
fig, ax = plt.subplots()
ax.plot(abs(error_n), abs(error_np1_predict),label="Theoretical Prediction")
ax.plot(abs(error_n), abs(error_np1),label="Experimental Prediction")
ax.legend()
ax.set_yscale('log')
ax.set_xscale('log')
ax.set(xlabel='error_n', ylabel='error_n+1')
plt.xlim(left=abs(error_n[-2]))
ax.grid()
plt.show()

    