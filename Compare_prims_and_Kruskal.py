import graph
import Prims
import Kruskal
import timeit
import pandas as pd
import matplotlib.pyplot as plt
numnodes = 14
density = 100
list_time_prims = []
list_time_kruskals = []
list_density = []
for i in range(density):
    calculate_density = i/100
    graph_generated = graph.generate_graph(numnodes, calculate_density)
    # Time complexity Prim's
    start_time1 = timeit.default_timer()
    prim_graph = Prims.prim(graph_generated)
    end_time1 = timeit.default_timer()
    list_time_prims.append(end_time1 - start_time1)

    # Time complexity Kruskal's
    start_time2 = timeit.default_timer()
    kruskal = Kruskal.kruskal(graph_generated)
    end_time2 = timeit.default_timer()
    list_time_kruskals.append(end_time2 - start_time2)
    list_density.append(calculate_density)

df = pd.DataFrame({'Density': list_density, 'Prims': list_time_prims, 'Kruskal': list_time_kruskals})
# Create scatter plot
plt.scatter(df['Density'], df['Prims'])
plt.scatter(df['Density'], df['Kruskal'])
plt.title('Compare Prims and Kruskal: numnodes = 14')
plt.xlabel('Density')
plt.ylabel('Time complexity')
plt.legend(['Prims', 'Kruskal'])
plt.grid(True)
plt.show()