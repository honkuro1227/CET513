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

print ("\n\n\nProblem3")
def Obj_func(xyz):
    x1,x2,x3=xyz
    f=2*x1+3*x2+x3
    print ("x1: "+str(x1)+"     x2: "+str(x2)+"     x3: "+str(x3))
    return f
def con(xyz):
    cons=({'type':'ineq','fun':lambda x: 2*x[0]+x[1]-x[2]-3},\
          {'type':'ineq','fun':lambda x: x[0]+x[1]+x[2]-2},\
          {'type':'ineq','fun':lambda x: x[2]},\
          {'type':'ineq','fun':lambda x: x[0]},\
          {'type':'ineq','fun':lambda x: x[1]})
    return cons

initial_guess=[0,4,0]# initial guess
cons=con(initial_guess)
res=minimize(Obj_func,initial_guess, constraints=cons)

print ("x: ",res.x)
print ("Obj_func :",Obj_func(res.x))
print ("\n\n\n")



print ("\n\n\nProblem3Dual")
def Obj_func(xy):
    x1,x2=xy
    f=-(3*x1+2*x2)
    print ("x1: "+str(x1)+"       x2: "+str(x2))
    return f
def con(xyz):
    cons=({'type':'ineq','fun':lambda x: -(2*x[0]+x[1]-2)},\
          {'type':'ineq','fun':lambda x: -(x[0]+x[1]-3)},\
          {'type':'ineq','fun':lambda x: -(-x[0]+x[1]-1)},\
          {'type':'ineq','fun':lambda x: x[0]},\
          {'type':'ineq','fun':lambda x: x[1]})
    return cons

initial_guess=[0,0]# initial guess
cons=con(initial_guess)
res=minimize(Obj_func,initial_guess, constraints=cons)

print ("x: ",res.x)
print ("Obj_func :",abs(Obj_func(res.x)))
print ("\n\n\n")
