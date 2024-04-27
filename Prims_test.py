import graph
import Prims

numnodes = 15
density = 0.8
percentage = 0.6
graph1 = graph.generate_negative_weighted_graph(numnodes, density, percentage)
print(graph1)

mst_graph = Prims.prim(graph1)
min_sum = 0
for i in range(1, len(mst_graph)):
        print(f"{mst_graph[i]} - {i} \t {graph1[i][mst_graph[i]]}")
        min_sum += graph1[i][mst_graph[i]]
print('Sum: ', min_sum)
