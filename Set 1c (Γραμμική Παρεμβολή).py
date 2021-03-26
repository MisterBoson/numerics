# Numerical Analysis Course - Physics Department Auth 
# Michael Chadolias  AEM: 14871
#
# Set 1st 
# Exercise 1c

import numpy as np


def f1(x):
    return 2*x+3*np.sin(4*x)-np.exp(x)

iteration = [0]

#initial condition
x= [0.5,1.0]
sol=[]

for i in range(0,10):
   x.append( x[i+1]- f1(x[i+1])/(f1(x[i+1])-f1(x[i]))*(x[i+1]-x[i]))
    
   
    
