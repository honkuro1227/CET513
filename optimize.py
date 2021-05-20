import pandas as pd
from mip import Model, xsum, minimize, BINARY
from math import cos,pi

#model Data
LocationS=[]
Destinations=[]
Hss=[]
Hse=[]
dists=[]
VariableC=[]
Order_ID=[]
hotspot=[(104.072455,30.6635),(104.09313,30.64376)]
Solution=[]

#cost variable
Vc=1.01*1.6#driver get
Mc=1.35*1.6# 1 miltes get
VcR=2.02*1.6
Sc=0.2# statisfy number
Tc=.24#time cost
Rsdiscount=0.52
Dc=1.35*1.6/1000# detour cost
#R=1

def distance(s,d):
    x1=s[0]
    y1=s[1]
    x2=d[0]
    y2=d[1]
    return pow((pow(100*(x1-x2),2)+pow(100*cos(110)*(y1-y2),2)),1/2)

#StartTime	endTime	startX	startY	endX	endY
def output_mfs(fs,name):
    result=fs.iloc[:]
    result.to_csv(name+'.csv', encoding='utf-8', index=False)
    return


def load_model():
    global VariableC,LocationS,Destinations,Hss,Hse,hotspot,dists
    default = pd.read_csv("1102_1000.csv", index_col = "Order_ID")
    default2= pd.read_csv("1102_1000_output.csv", index_col = "Order_ID")
    default3= pd.read_csv("1102_1000_output.csv")
    default.rename(columns=lambda x:x.lower(),inplace=True)
    default2.rename(columns=lambda x:x.lower(),inplace=True)
    for p in range(len(default2['cost'])):
        VariableC.append(default2['cost'][p])
        
    for p in range(len(default3['Order_ID'])):
        Order_ID.append(default3['Order_ID'][p])    
    for p in range(len(default['starttime'])):
        LocationS.append((default['startx'][p],default['starty'][p]))
        Destinations.append((default['endx'][p],default['endy'][p]))
        Hss.append(distance(LocationS[p],hotspot[0]))
        Hse.append(distance(Destinations[p],hotspot[1]))
        dists.append(distance(LocationS[p],Destinations[p]))
load_model()
ovalue=0
for i in range(len(LocationS)):
    ovalue+=VariableC[i]*Mc-Vc*dists[i]
Maxvalue=float('-inf')
MaxR=0
for R in range(1,100):

    model=Model()
    B=[model.add_var(var_type=BINARY)  for i in range(len(LocationS))]


    model.objective=minimize(xsum(
            B[i]*VcR*(1-Rsdiscount)*dists[i]+\
            (1-B[i])*Vc*dists[i]+B[i]*Sc/(R/2)*(Hss[i]+Hse[i])\
            +Dc*R*B[i]\
            for i in range(len(LocationS))
            )
    )    
    
    model += xsum(
            B[i]*VcR*(1-Rsdiscount)*dists[i]+\
            (1-B[i])*Vc*dists[i]+B[i]*Sc/(R/2)*(Hss[i]+Hse[i])\
            +Dc*R*B[i]\
            for i in range(len(LocationS))
            ) >= 0
    model.optimize()
    value=0
    for i in range(len(LocationS)):
        value+=VariableC[i]*Mc-model.objective_value
    if value>Maxvalue:
        Maxvalue=value
        MaxR=R
        Solution.clear()
        for i in range(len(LocationS)):
            Solution.append([i,B[i].x])
    print(value)
    
# result
count=0
x_id=[]
y_pred_prob=[]
for s in range(len(LocationS)):
    if Solution[s][1]==1:
        count+=1
    x_id.append(Order_ID[s])
    y_pred_prob.append(round(Solution[s][1]))
dic={
    "Order_ID":x_id,
    "rideshare":y_pred_prob
    }

output_mfs(pd.DataFrame(dic),'result')
od=0
for s in range(len(LocationS)):
    od+=dists[i]

rd=0
for s in range(len(LocationS)):
    if round(Solution[s][1])==1:
        rd+=(distance(hotspot[0],hotspot[1])+Hss[s]+Hse[s])*Rsdiscount
    else:
        rd+=dists[i]
print("Radius :",MaxR/100)
print("Rideshare Distance :"+str(rd))        
print("Revenue :"+str(round(Maxvalue)/100)+" dollars ")
print("Number of Rideshare: "+str(count)+" Ratio of Rideshares/Total Trips: "+str(round(count/len(LocationS)*100))+" %")
print("Original Revenue is: ",round(ovalue/100))
print("Original Distance is :"+str(od))   
    
    
    
    
    
    
    
    
