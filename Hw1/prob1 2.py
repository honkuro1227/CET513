# -*- coding: utf-8 -*-
"""
probl1 2.py
by Hung Lo
UWNetID: honkuro
Student number: 1926128

Assignment 1, in CET 513, Autumn 2019.
 
This file contains my problem formulation for the problem of
1 and 2
"""

#todo problem1
"""
t1=1+0.01v1
t2=10+0.005v2
v1+v2=3900
persue the mini t1+t2 and give flow distribute of vehicles
"""
import math
import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize, basinhopping


print ("Problem1\n")
def f(x):
    return (1+0.01*x)+(10+0.005*(3900-x))
x=np.arange(0,3901,1)

plt.plot(x, f(x)) #draw 
plt.show() #print draw
result1=minimize(f,x0=0, bounds =([0,3901],))

print('solution v1=')
print(result1.x)
print('objective value =')
print(f(result1.x))
"""
for x in range(3901):
    v1=x
    v2=3900-x
    t2=10+0.005*v2
    t1=1+0.01*v1
    ttime=t2+t1
    if ttime<result:
        result=ttime
        minix=x
        
    #print ("v1 :"+str(v1)+" v2: "+str(v2)+" ttime: "+str(ttime))

"""
#todo problem2
#OPTIMISATION USING SCIPY
"""
Variables:
    Labor hour=x
    items=x**0.5*K**(1/3)
    Income=80*Q
    capital cost=5
    if(x<=160):
        Labor cost=15
    if(x>160):
        Labor cost=25
    Total Cost=Labor Cost*x+5*capital hour
    Revenue=Income-Total Cost
"""
print ("\n\n\nProblem2")
def Obj_func(xy):
    x,y=xy
    f=-80*(x**0.5*y**(1/3))+15*x+5*y# Let minimize work
    return f
initial_guess=[1,1]# initial guess
bnds = ((0, 160), (0, None))#bounds Labor hours>0, capital hours >0
res=minimize(Obj_func,initial_guess, bounds=bnds)
print ("When labor hour<=160, Result: \n",res.x)
print ("Revenue: ",abs(Obj_func(res.x)))
print ("\n\n\n")
initial_guess2=[161,1]
def Obj_func2(xy):
    x,y=xy
    f=-80*(x**0.5*y**(1/3))+25*(x-160)+5*y+15*160
    return f
bnds = ((161, None), (0, None))
res2=minimize(Obj_func2,initial_guess2, bounds=bnds)
print ("When labor hour>160, Result: \n",res2.x)
print  ("Revenue: ",abs(Obj_func2(res2.x)))





    
    
    


