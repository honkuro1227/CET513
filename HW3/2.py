#import matplotlib.pyplot as plt

import numpy as np
#from scipy.optimize import minimize


def obj(x):
    return 4*pow((x[0]-10),2)+pow((x[1]-4),2)
def gradient(x):
    return [8*(x[0]-10), 2*(x[1]-4)]

#x = np.arange(-0.5, 1.5, 0.1)
#plt.plot(x, f(x))
#plt.show()

# initial point (0,0)
n=2
x0 = np.zeros(n);
alpha=0.1

value=[0,0]
for i in range(100):
    value[0]=value[0]-alpha*gradient(value)[0]
    value[1]=value[1]-alpha*gradient(value)[1]
    print(i+1,"th iteration :")
    print("alpha is :", alpha)
    print("X is ",value[0],"Y is ",value[1])
    print("Objective value is",obj(value))
## solve for the minimizer
#result1 = minimize(obj, x0, method ='SLSQP')
#
#x = result1.x;
#
#print('x1 = ' + str(x[0]) + '; x2= ' + str(x[1]))
#print('Optimal Objective Value = ' + str(obj(x)))
#
#print('\n')
#
#
## 2nd Example
#def obj2(x):
#    return 0.5*(x[0]**2 - x[1]**2) - x[1]
#
#result2 = minimize(obj2, x0, method ='SLSQP')
#
#x2 = result2.x;
#
#print('x1 = ' + str(x2[0]))
#print('x2 = ' + str(x2[1]))
#print('Optimal Objective Value = ' + str(obj2(x2)))
#
#print('\n')