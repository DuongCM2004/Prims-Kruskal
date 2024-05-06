import pandas as pd
import graph
import Prims
import Kruskal
import matplotlib.pyplot as plt

numnodes = 15
density = 100
prims = []
kruskal = []
index = []
for i in range(40, density):
    calculate_density = i/100
    min_sum_list = []
    min_sum_list1 = []
    for j in range(10):
        graph1 = graph.generate_graph(numnodes, calculate_density)
        mst_graph = Prims.prim(graph1)
        min_sum = 0
        for a in range(len(mst_graph)):
                min_sum += mst_graph[a][2]
        min_sum_list.append(min_sum)


        #Test Kruskal
        mst_graph2 = Kruskal.kruskal(graph1)
        min_sum1 = 0
        for b in range(len(mst_graph2)):
                min_sum1 += mst_graph2[b][2]
        min_sum_list1.append(min_sum1)
    prims.append(sum(min_sum_list)/len(min_sum_list))
    kruskal.append(sum(min_sum_list1)/len(min_sum_list1))
    index.append(i)
df = pd.DataFrame({'node': index, 'prims': prims,'kruskal': kruskal})

# Plot the data
plt.plot(df['node'], df['prims'], label='prims', color='blue')
# Add labels and title
plt.xlabel('Density')
plt.ylabel('Average Weight')
plt.title("Prim's Algorithm: Average Weight vs. Density")

# Show the plot
plt.grid(True)
plt.legend()
plt.show()

plt.plot(df['node'], df['kruskal'], label='kruskal', color='red')
# Add labels and title
plt.xlabel('Density')
plt.ylabel('Average Weight')
plt.title("Prim's Algorithm: Average Weight vs. Density")
# Show the plot
plt.grid(True)
plt.legend()
plt.show()