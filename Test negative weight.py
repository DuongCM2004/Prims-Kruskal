import graph
import Prims
import Kruskal
import Visualize as Vi

numnodes = 15
density = 0.8
percentage = 0.3
graph1 = graph.generate_negative_weighted_graph(numnodes, density, percentage)
print(graph1)

# Test Prims
mst_graph = Prims.prim(graph1)
min_sum = 0
for i in range(1, len(mst_graph)):
        print(f"{mst_graph[i]} - {i} \t {graph1[i][mst_graph[i]]}")
        min_sum += graph1[i][mst_graph[i]]
print('Sum: ', min_sum)


#Test Kruskal
mst_graph2 = Kruskal.kruskal(graph1)
min_sum1 = 0
for i in range(len(mst_graph2)):
        print(f"{mst_graph2[i][0]} - {mst_graph2[i][1]} \t {mst_graph2[i][2]}")
        min_sum1 += mst_graph2[i][2]
print('Sum1: ', min_sum1)

Vi.visualize_mst(graph1, mst_graph)
Vi.visualize_mst_list(graph1, mst_graph2)
