# for the maximum flow problem

from ortools.graph import pywrapgraph

#def main():
# instantinae a SimpleMinCostFlow Solver
max_flow = pywrapgraph.SimpleMaxFlow()

# define four parallel arrays: start_nodes, end_nodes, capacities, and unit_cost
# for each link.
# Note: node number has to start from zero!
start_nodes = [0 , 0 , 0 , 1, 1, 1 , 2, 2, 3, 4 , 4 , 5 , 5 ]
end_nodes =   [1 , 2 , 3 , 3, 4, 5 , 1, 5, 4, 5 , 6 , 4 , 6 ]
capacities =  [20, 15, 10, 4, 5, 9 , 5, 6, 8, 25, 10, 5 , 30]
#unit_cost = [1, 1, 1, 1, 1, 1, 1, 1]

# add each link
for i in range(0, len(start_nodes)):
    max_flow.AddArcWithCapacity(start_nodes[i], end_nodes[i], capacities[i])

# solve
if max_flow.Solve(0, 6) == max_flow.OPTIMAL:
    print('Max Flow:', max_flow.OptimalFlow())
    print(' ')
    print('  Arc    Flow / Capacity')
    for i in range(max_flow.NumArcs()):
      print('%1s -> %1s   %3s  / %3s' % (
            max_flow.Tail(i)+1,
            max_flow.Head(i)+1,
            max_flow.Flow(i),
            max_flow.Capacity(i)))
    result=[[],[]]
    for i in max_flow.GetSourceSideMinCut():
        result[0].append(i+1)
    for i in max_flow.GetSinkSideMinCut():
        result[1].append(i+1)
    print('Source side min-cut:', result[0])
    print('Sink side min-cut:', result[1])
else:
    print('There was an issue with the max flow input.')
    

