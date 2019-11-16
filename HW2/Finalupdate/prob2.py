# -*- coding: utf-8 -*-
"""
prob2.py
by Hung Lo
UWNetID: honkuro
Student number: 1926128

Assignment 1, in CET 513, Autumn 2019.
 
This file contains my problem formulation for the problem of 2
"""


import math
import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize, basinhopping

print ("\n\n\nProblem2")
def Obj_func(xy):
    x1,x2=xy
    f=2*x1+x2
    print ("x1: "+str(x1)+"x2: "+str(x2))
    return f
def con(xy):
    cons=({'type':'ineq','fun':lambda x: -4*x[0]+12*x[1]-6},\
          {'type':'ineq','fun':lambda x: 4*x[0]-6*x[1]+12},\
          {'type':'ineq','fun':lambda x: 4*x[0]+2*x[1]-8},\
          {'type':'ineq','fun':lambda x: -x[0]-x[1]+9},\
          {'type':'ineq','fun':lambda x: -x[1]+4},\
          {'type':'ineq','fun':lambda x: x[0]},\
          {'type':'ineq','fun':lambda x: x[1]})
    return cons

initial_guess=[0,4]# initial guess
cons=con(initial_guess)
res=minimize(Obj_func,initial_guess, constraints=cons)

print ("x: ",res.x)
print ("Obj_func :",round(Obj_func(res.x)))
print ("\n\n\n")
y =[]
plt.plot(res.x[0],res.x[1], marker='o', markerfacecolor='green', markersize=12) 

x1 = np.arange(-1, 10,0.1 )
y1 =[]
for s in x1:
    y1.append(4)
plt.plot(x1,y1) 
x2 = np.arange(-1, 10,0.1 )
y2 =[]
for s in x2:
    y2.append(0)

plt.plot(x2,y2,label="x2=0")

x3 = np.arange(-1, 5,0.1 )
y3 =[]
for s in x3:
    y3.append(0)
plt.plot(y3,x3,label="x1=0")

x4 = np.arange(4, 10,0.1 )
y4 =[]
for s in x4:
    y4.append(9-s)
    if round(9-s)==4:
        plt.plot(round(s),round(9-s), marker='o', markerfacecolor='red', markersize=12)
   
plt.plot(x4,y4,label="line x1+x2=9") 

x5 = np.arange(-1, 3,0.1 )
y5 =[]
for s in x5:
    y5.append(4-2*s)
    if s>=0.75 and s<=27/14:
        plt.plot(s,4-2*s, marker='o', markerfacecolor='green', markersize=12)

plt.plot(x5,y5,label="line 4x1+2x2=8") 

x6 = np.arange(-1,10,0.1 )
y6 =[]
for s in x6:
    y6.append((4*s-6)/12)
plt.plot(x6,y6,label="line 4x1-12x2=6") 

x7 = np.arange(-1,10,0.1 )
y7 =[]
for s in x7:
    y7.append((6+2*s)/3)
plt.plot(x7,y7,label="line -4x1+6x2=12") 
plt.plot(3,4, marker='o', markerfacecolor='purple', markersize=12)
plt.plot(27/14,1/7, marker='o', markerfacecolor='yellow', markersize=12)
plt.plot(57/8,15/8, marker='o', markerfacecolor='blue', markersize=12)

plt.legend()
plt.xlabel('x1 -axis')
plt.ylabel('x2 -axis')
plt.show()





    
    
    


