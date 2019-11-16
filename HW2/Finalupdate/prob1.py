# -*- coding: utf-8 -*-
"""
prob1.py
by Hung Lo
UWNetID: honkuro
Student number: 1926128

Assignment 2, in CET 513, Autumn 2019.
 
This file contains my problem formulation for the problem of 1 
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize, basinhopping

print ("\n\n\nProblem1")
def Obj_func(xy):
    x1,x2=xy
    f=20000*x1+10000*x2
    print ("x1: "+str(x1)+"x2: "+str(x2))
    return f
def con(xy):
    cons=({'type':'ineq','fun':lambda x: x[0]+x[1]-100},\
          {'type':'ineq','fun':lambda x: x[0]-50},\
          {'type':'ineq','fun':lambda x: -2+0.02*x[0]+0.02*x[1]},\
          {'type':'ineq','fun':lambda x: x[1]-35})
    return cons

initial_guess=[100,100]# initial guess
cons=con(initial_guess)
res=minimize(Obj_func,initial_guess, constraints=cons)

print ("x: ",res.x)
print ("Obj_func :",Obj_func(res.x))
print ("\n\n\n")
x = np.arange(35,100,0.1 )
y =[]
for s in x:
    y.append(35)
plt.plot(x,y,label="line ε_2=35%") 

x = np.arange(35,100,0.1 )
y =[]
for s in x:
    y.append(50)
plt.plot(y,x,label="line ε_1=50%") 

x = np.arange(35,100,0.1 )
y =[]
for s in x:
    y.append(35)
plt.plot(y,x,label="line ε_1=35%") 

x = np.arange(34,100,1 )
y =[]
for s in x:
    y.append((2-0.02*s)/0.02)
plt.plot(x,y,label="line 0.02ε_1+0.02ε_2+2=4") 
plt.xlabel('ε_1 -axis')
plt.ylabel('ε_2 -axis')
plt.plot(res.x[0],res.x[1], marker='o', markerfacecolor='purple', markersize=12)
plt.legend()
plt.show()





    
    
    


