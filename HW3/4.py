
def f(x):
    return 65*x**6 + 71*x**5 -322*x**4 - 401*x**3
def g(x):
    return 390*x**5 + 355*x**4 -1288*x**3 - 1203*x**2

def bisection(alpha=0,beta=3,errorstop=0.0001):
    value=0
    c=(alpha+beta)/2
    if (abs(alpha-c)<errorstop):
        print("stop! the error between alpha and mean is",abs(alpha-c))
        return alpha
   
    if (abs(beta-c)<errorstop):
        print("stop! the error between alpha and mean is",abs(beta-c))
        return beta
    fa=g(alpha)
    fb=g(beta) 
    fc=g(c)
    print(" fa:",fa," fb: ",fb," fc: ",fc)
    print("alpha : ",alpha,"  beta : ",beta," mean of alpha and beta: ",c)

    if(fa*fc>=0):
        print("update alpha ",alpha," with mean :",c)
        value=bisection(c,beta)
    if(fb*fc>=0):
        print("update beta ",beta," with mean :",c)
        value=bisection(alpha,c)
        
    return value

value=bisection()
print("x :"+str(value))
print("f(x) "+str(f(value)))
