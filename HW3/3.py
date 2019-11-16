
from mip import Model, xsum, minimize, BINARY
from itertools import combinations

def distance(s,d):
    x1=s[0]
    y1=s[1]
    x2=d[0]
    y2=d[1]
    return pow((pow(abs(x1-x2),2)+pow(abs(y1-y2),2)),1/2)


supply=[49,874,555,352,381,428,985,105,258,210]
FixC=[2000000,1000000,1000000,1000000,3000000,2000000,1000000,2000000,4000000,2000000]
VariableC=[310,40,51,341,131,182,20,40,177,75]
Location=[(4,3),(2,5),(10,8),(2,8),(5,3),(4,5),(10,5),(5,1),(5,8),(1,7)]
Bk={0,1,2}
n = len(FixC)
cm=[0,1,2,3,4,5,6,7,8,9]
valuemin=float('inf')
result=[]
for ct in range(3,11):
    ree=[]
    dists=[[0 if i==j
            else distance(Location[i],Location[j])
            for j in range(10)]for i in range(10)]


    total=list(combinations([0,1,2,3,4,5,6,7,8,9],5))
    for k in total:
        retE = [i for i in cm if i not in list(k)]
        ree.append(retE)
    
#print(re)
#for k in total:
#    tt.append(list(k))
##re.append(list(total[0]))
##print(re)
##print(total)
#print(tt)

    for re in ree:

        model = Model()
        B= [[model.add_var(var_type=BINARY) for j in range(10)] for i in range(10)]
        model.objective = minimize(xsum(((dists[i][j]*1000+VariableC[j])*B[i][j]*supply[i] for i in range(10) for j in range(10))))
    
        for i in range(10):
            model += xsum(B[j][i]*supply[j] for j in set(range(10))) <= 1500

        for i in range(10):
            model += xsum(B[j][i]*supply[j] for j in set(range(10))) >= 0
    
        for i in range(10):
            model += xsum(B[i][j] for j in set(range(10))) == 1


        for p, k in enumerate(re):
            model += xsum(B[i][j] for i in range(10) for j in range(10) if  j == k) == 0, 'diag2({} )'.format(p)
    
        model.optimize()

        #print("variablecost : ",model.objective_value)


        value=model.objective_value
        retE2 = [i for i in cm if i not in list(re)]
        for kk in retE2:
            value+=FixC[kk]

        if value<valuemin:
            valuemin=value
            result.clear()
            for i in range(10):
                for j in range(10):
                    if(B[i][j].x==0): continue
                    result.append([i,j,B[i][j].x,retE2])
        #print("value :",value)
    
print(valuemin)
for s in result:
    print("i :"+str(s[0]+1)+" j: "+str(s[1]+1)+" "+str(s[2]))
value=0
#print(result[3])
for s in result[0][3]:
    value+=FixC[int(s)]
    print("Fixc s:  ",s+1," value :",FixC[int(s)])
for s in result:
    print(" i : ",s[0]+1,"  j: ",s[1]+1," supply is ",supply[s[0]]," dists :",dists[s[0]][s[1]]," val= " ,(dists[s[0]][s[1]]*1000+VariableC[s[1]])*s[2]*supply[s[0]])
    value+=(dists[s[0]][s[1]]*1000+VariableC[s[1]])*s[2]*supply[s[0]]
print(value)