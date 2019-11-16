# for the minimum cost flow problem

from ortools.graph import pywrapgraph

#def main():
# instantinae a SimpleMinCostFlow Solver
min_cost_flow = pywrapgraph.SimpleMinCostFlow()

# define four parallel arrays: start_nodes, end_nodes, capacities, and unit_cost
# for each link.
# Note: node number has to start from zero!
start_nodes = [0, 0, 1, 1, 2, 2, 3, 3, 3, 4, 5]
end_nodes =   [1, 2, 2, 3, 1, 4, 2, 4, 5, 3, 4]
capacities =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 
unit_cost =   [2, 8, 5, 3, 6, 0, 1, 7, 6, 4, 2]

# add each link
for i in range(0, len(start_nodes)):
    min_cost_flow.AddArcWithCapacityAndUnitCost(start_nodes[i], end_nodes[i], capacities[i], unit_cost[i])

# add supplies:
supplies = [1, 0, 0, 0, 0, -1]
for i in range(0, len(supplies)):
    min_cost_flow.SetNodeSupply(i, supplies[i])


# solve
if min_cost_flow.Solve() == min_cost_flow.OPTIMAL:
    print('Minimum cost:', min_cost_flow.OptimalCost())
    print(' ')
    print('  Arc    Flow / Capacity  Cost')
    for i in range(min_cost_flow.NumArcs()):
      cost = min_cost_flow.Flow(i) * min_cost_flow.UnitCost(i)
      print('%1s -> %1s   %3s  / %3s       %3s' % (
            min_cost_flow.Tail(i)+1,
            min_cost_flow.Head(i)+1,
            min_cost_flow.Flow(i),
            min_cost_flow.Capacity(i),
            cost))
else:
    print('There was an issue with the min cost flow input.')
    

