# for the minimum cost flow problem

from ortools.graph import pywrapgraph

#def main():
# instantinae a SimpleMinCostFlow Solver
min_cost_flow = pywrapgraph.SimpleMinCostFlow()

# define four parallel arrays: start_nodes, end_nodes, capacities, and unit_cost
# for each link.
# Note: node number has to start from zero!
start_nodes = [1,1,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,8,8,8,8,9,9,9,10,10,10,10,10,11,11,11,11,12,12,12,13,13,14,14,14,15,15,15,15,16,16,16,16,17,17,17,18,18,18,19,19,19,20,20,20,20,21,21,21,22,22,22,22,23,23,23,24,24,24]
end_nodes =   [2, 3, 1, 6, 1, 4, 12, 3, 5, 11, 4, 6, 9, 2, 5, 8, 8, 18, 6, 7, 9, 16, 5, 8, 10, 9, 11, 15, 16, 17, 4, 10, 12, 14, 3, 11, 13, 12, 24, 11, 15, 23, 10, 14, 19, 22, 8, 10, 17, 18, 10, 16, 19, 7, 16, 20, 15, 17, 20, 18, 19, 21, 22, 20, 22, 24, 15, 20, 21, 23, 14, 22, 24, 13, 21, 23
]
capacities = [25900.20064, 23403.47319, 25900.20064, 4958.180928, 23403.47319, 17110.52372, 23403.47319, 17110.52372, 17782.7941, 4908.82673, 17782.7941, 4947.995469, 10000, 4958.180928, 4947.995469, 4898.587646, 7841.81131, 23403.47319, 4898.587646, 7841.81131, 5050.193156, 5045.822583, 10000, 5050.193156, 13915.78842, 13915.78842, 10000, 13512.00155, 4854.917717, 4993.510694, 4908.82673, 10000, 4908.82673, 4876.508287, 23403.47319, 4908.82673, 25900.20064, 25900.20064, 5091.256152, 4876.508287, 5127.526119, 4924.790605, 13512.00155, 5127.526119, 14564.75315, 9599.180565, 5045.822583, 4854.917717, 5229.910063, 19679.89671, 4993.510694, 5229.910063, 4823.950831, 23403.47319, 19679.89671, 23403.47319, 14564.75315, 4823.950831, 5002.607563, 23403.47319, 5002.607563, 5059.91234, 5075.697193, 5059.91234, 5229.910063, 4885.357564, 9599.180565, 5075.697193, 5229.910063, 5000, 4924.790605, 5000, 5078.508436, 5091.256152, 4885.357564, 5078.508436
]
unit_cost = [6, 4, 6, 5, 4, 4, 4, 4, 2, 6, 2, 4, 5, 5, 4, 2, 3, 2, 2, 3, 10, 5, 5, 10, 3, 3, 5, 6, 4, 8, 6, 5, 6, 4, 4, 6, 3, 3, 4, 4, 5, 4, 6, 5, 3, 3, 5, 4, 2, 3, 8, 2, 2, 2, 3, 4, 3, 2, 4, 4, 4, 6, 5, 6, 2, 3, 3, 5, 2, 4, 4, 4, 2, 4, 3, 2
]

for i in range(0, len(capacities)):
    capacities[i] = round(capacities[i])
    start_nodes[i]=start_nodes[i]-1
    end_nodes[i]= end_nodes[i]-1

# add each link
for i in range(0, len(start_nodes)):
    min_cost_flow.AddArcWithCapacityAndUnitCost(start_nodes[i], end_nodes[i], capacities[i], unit_cost[i])

supplies=[]
for i in range(24):
    supplies.append(0)
supplies[0]=1

for il in range(len(supplies)-1):
    supplies[il+1]=-1
    #print(supplies)
    for i in range(0, len(supplies)):
        min_cost_flow.SetNodeSupply(i, supplies[i])
# solve
    if min_cost_flow.Solve() == min_cost_flow.OPTIMAL:
        
        print(' ')
        print('  Arc    Flow / Capacity  Cost')
        for i in range(min_cost_flow.NumArcs()):
            cost = min_cost_flow.Flow(i) * min_cost_flow.UnitCost(i)
            if(min_cost_flow.Flow(i)==1):
                print('%1s -> %1s   %3s  / %3s       %3s' % (
                        min_cost_flow.Tail(i)+1,
                        min_cost_flow.Head(i)+1,
                        min_cost_flow.Flow(i),
                        min_cost_flow.Capacity(i),
                        cost))
        print('Minimum cost:', min_cost_flow.OptimalCost())
    else:
        print('There was an issue with the min cost flow input.')
    supplies[il+1]=0
    

