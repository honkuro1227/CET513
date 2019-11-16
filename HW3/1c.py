# for the minimum cost flow problem

from ortools.graph import pywrapgraph
import random
costr=[1,2,3,4,5,6,7,8,9,10]
#def main():
# instantinae a SimpleMinCostFlow Solver
min_cost_flow = pywrapgraph.SimpleMinCostFlow()

# define four parallel arrays: start_nodes, end_nodes, capacities, and unit_cost
# for each link.
# Note: node number has to start from zero!
start_nodes = [0 , 0 , 0 , 1, 1, 1 , 2, 2, 3, 4 , 4 , 5 , 5 ]
end_nodes =   [1 , 2 , 3 , 3, 4, 5 , 1, 5, 4, 5 , 6 , 4 , 6 ]
capacities =  [20, 15, 10, 4, 5, 9 , 5, 6, 8, 25, 10, 5 , 30]
unit_cost =   []

# add each link
for i in range(0, len(start_nodes)):
    unit_cost.append(random.choice(costr))
for i in range(0, len(start_nodes)):
    min_cost_flow.AddArcWithCapacityAndUnitCost(start_nodes[i], end_nodes[i], capacities[i], unit_cost[i])

# add supplies:
supplies = [10, 5, 0, 0, -3, -7, -5]
for i in range(0, len(supplies)):
    min_cost_flow.SetNodeSupply(i, supplies[i])


# solve
if min_cost_flow.Solve() == min_cost_flow.OPTIMAL:
    print('Minimum cost:', min_cost_flow.OptimalCost())
    print(' ')
    print('  Arc    Flow / Capacity  Cost  unit_cost')
    for i in range(min_cost_flow.NumArcs()):
      cost = min_cost_flow.Flow(i) * min_cost_flow.UnitCost(i)
      print('%1s -> %1s   %3s  / %3s       %3s  %3s' % (
            min_cost_flow.Tail(i)+1,
            min_cost_flow.Head(i)+1,
            min_cost_flow.Flow(i),
            min_cost_flow.Capacity(i),
            cost,
            min_cost_flow.UnitCost(i)))
else:
    print('There was an issue with the min cost flow input.')
    

