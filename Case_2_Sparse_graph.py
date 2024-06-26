import graph
import Prims
import Kruskal
import Visualize as Vi

numnodes = 10
density = 0.3
graph1 = graph.generate_graph(numnodes,density)
print(graph1)

# Test Prims
mst_graph = Prims.prim(graph1)
min_sum = 0
for i in range(len(mst_graph)):
        print(f"{mst_graph[i][0]} - {mst_graph[i][1]} \t {mst_graph[i][2]}")
        min_sum += mst_graph[i][2]
print('Sum: ', min_sum)


#Test Kruskal
mst_graph2 = Kruskal.kruskal(graph1)
min_sum1 = 0
for i in range(len(mst_graph2)):
        print(f"{mst_graph2[i][0]} - {mst_graph2[i][1]} \t {mst_graph2[i][2]}")
        min_sum1 += mst_graph2[i][2]
print('Sum1: ', min_sum1)

Vi.visualize(graph1, mst_graph, mst_graph2)