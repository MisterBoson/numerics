# Numerical Analysis Course - Physics Department Auth 
# Michael Chadolias  AEM: 14871
#
# Set 1st 
# Exercise 1b

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def func(x):
    return 2*x+3*np.sin(4*x)-np.exp(x)

#main
diff= [10**(-3),10**(-6),10**(-12)]
iteration= [1]
a ,b ,index= 0.5, 1.0 , 1
distance= [a,b]
fun=[] #function
sol=[] 
mesos= np.average(distance)
notification=[0,0]

while True:
    if (func(distance[0])*func(mesos))<0:
        distance[-1]= mesos
        fun.append(func(mesos))
        sol.append(mesos)
       # print('%.d %.16f'% (iteration[-1], func(mesos)))
        mesos= np.average(distance)
    else:
        distance[0]= mesos
        fun.append(func(mesos))
        sol.append(mesos)
      #  print('%.d %.16f'% (iteration[-1], func(mesos)))
        mesos= np.average(distance)
    if iteration[-1]>2:
        if (np.abs(fun[-1]-fun[-2])<diff[-1]):
            break   
        elif  (np.abs(fun[-1]-fun[-2])<diff[-2]): 
            if notification[0]==0:
                print("For error",diff[-2],"the iteration must reach:",'%.d %.16f'%(iteration[-1], sol[-1]))
                notification[0]=1
        elif  (np.abs(fun[-1]-fun[-2])<diff[-3]):
            if notification[1]==0:
                print("For error", diff[-3] ,"the iteration must reach:",'%.d %.16f'%(iteration[-1], sol[-1]))
                notification[1]=1
    iteration.append(index)
    index= index+1    
print("For error",diff[-1],"the iteration must reach:",'%.d %.16f'%(iteration[-1], sol[-1]))

N = len(sol)
error = sol[N-1]-sol
fig, ax = plt.subplots()
ax.plot(iteration, abs(error))
ax.set_yscale('log')
ax.set(xlabel='iteration', ylabel='error')
ax.grid()
plt.xlim(right=N-2)
tick_spacing = 1
ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
plt.show()