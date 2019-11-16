# for the maximum flow problem on the Sioux Falls network

from ortools.graph import pywrapgraph

#def main():
# instantinae a SimpleMinCostFlow Solver
max_flow = pywrapgraph.SimpleMaxFlow()

# define four parallel arrays: start_nodes, end_nodes, capacities, and unit_cost
# for each link.
# Note: node number has to start from zero!
start_nodes = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 13, 13, 14, 14, 14, 15, 15, 15, 15, 16, 16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 20, 20, 21, 21, 21, 22, 22, 22, 22, 23, 23, 23, 24, 24, 24
]
end_nodes = [2, 3, 1, 6, 1, 4, 12, 3, 5, 11, 4, 6, 9, 2, 5, 8, 8, 18, 6, 7, 9, 16, 5, 8, 10, 9, 11, 15, 16, 17, 4, 10, 12, 14, 3, 11, 13, 12, 24, 11, 15, 23, 10, 14, 19, 22, 8, 10, 17, 18, 10, 16, 19, 7, 16, 20, 15, 17, 20, 18, 19, 21, 22, 20, 22, 24, 15, 20, 21, 23, 14, 22, 24, 13, 21, 23
]
capacities = [25900.20064, 23403.47319, 25900.20064, 4958.180928, 23403.47319, 17110.52372, 23403.47319, 17110.52372, 17782.7941, 4908.82673, 17782.7941, 4947.995469, 10000, 4958.180928, 4947.995469, 4898.587646, 7841.81131, 23403.47319, 4898.587646, 7841.81131, 5050.193156, 5045.822583, 10000, 5050.193156, 13915.78842, 13915.78842, 10000, 13512.00155, 4854.917717, 4993.510694, 4908.82673, 10000, 4908.82673, 4876.508287, 23403.47319, 4908.82673, 25900.20064, 25900.20064, 5091.256152, 4876.508287, 5127.526119, 4924.790605, 13512.00155, 5127.526119, 14564.75315, 9599.180565, 5045.822583, 4854.917717, 5229.910063, 19679.89671, 4993.510694, 5229.910063, 4823.950831, 23403.47319, 19679.89671, 23403.47319, 14564.75315, 4823.950831, 5002.607563, 23403.47319, 5002.607563, 5059.91234, 5075.697193, 5059.91234, 5229.910063, 4885.357564, 9599.180565, 5075.697193, 5229.910063, 5000, 4924.790605, 5000, 5078.508436, 5091.256152, 4885.357564, 5078.508436
]
unit_cost = [6, 4, 6, 5, 4, 4, 4, 4, 2, 6, 2, 4, 5, 5, 4, 2, 3, 2, 2, 3, 10, 5, 5, 10, 3, 3, 5, 6, 4, 8, 6, 5, 6, 4, 4, 6, 3, 3, 4, 4, 5, 4, 6, 5, 3, 3, 5, 4, 2, 3, 8, 2, 2, 2, 3, 4, 3, 2, 4, 4, 4, 6, 5, 6, 2, 3, 3, 5, 2, 4, 4, 4, 2, 4, 3, 2
]

# round capacities to integer numbers
for i in range(0, len(capacities)):
    capacities[i] = round(capacities[i])

# add each link
for i in range(0, len(start_nodes)):
    max_flow.AddArcWithCapacity(start_nodes[i], end_nodes[i], capacities[i])

# solve
if max_flow.Solve(2, 13) == max_flow.OPTIMAL:

    print('Max Flow:', max_flow.OptimalFlow())
    print(' ')
    print('  Arc       Flow / Capacity')
    for i in range(max_flow.NumArcs()):
      print('%2s -> %2s   %6s  / %6s' % (
            max_flow.Tail(i),
            max_flow.Head(i),
            max_flow.Flow(i),
            max_flow.Capacity(i)))
    print('Source side min-cut:', max_flow.GetSourceSideMinCut())
    print('Sink side min-cut:', max_flow.GetSinkSideMinCut())
else:
    print('There was an issue with the max flow input.')
    

