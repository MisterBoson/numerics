# Numerical Analysis Course - Physics Department Auth 
# Michael Chadolias  AEM: 14871
#
# Set 1st 
# Exercise 3a

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from sympy import *
"""
x= Symbol("x")
y= Symbol("y")

f=2*x-exp(x)+3-y
g=0.5*x-2*x**3-y
"""
#functions and derivatives
def f1(x,y):
    return 2*x-np.exp(x)+3-y
def g1(x,y):
    return 0.5*x-2*x**3-y
def fx(x):
    return 2-3*np.exp(x)
def gx(x):
    return 0.5-6*x**2
fy,gy=-1,-1

#initial conditions
x,y=0.5,0.5

for i in range(0,20):
    xnew =  x - (f1(x,y)*gy-g1(x,y)*fy)/(fx(x)*gy-gx(x)*fy)
    ynew =  y - (g1(x,y)*gx(x)-f1(x,y)*g1(x,y))/(fx(x)*gy-gx(x)*fy)
    x = xnew
    y = ynew
    print('%.16f'% x, '%.16f'% y)
