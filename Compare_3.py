import graph
import Prims
import Kruskal
import matplotlib.pyplot as plt
import pandas as pd

numnodes = 15
density = 100
index = []
prims = []
kruskal = []
for i in range(20, density):
    calculate_density = i/100
    ge_graph = graph.generate_graph(numnodes, calculate_density)
    # Store Prims comparison
    prims_comparison = Prims.prim_comparision(ge_graph)
    prims.append(prims_comparison)

    # Store Kruskal comparison
    kruskal_comparison = Kruskal.kruskal_comparison(ge_graph)
    kruskal.append(kruskal_comparison)

    # Store index
    index.append(calculate_density)

# Draw graph
df = pd.DataFrame({'density': index, 'prims': prims, 'kruskal': kruskal})

# Plot the data
plt.plot(df['density'], df['prims'], label='prims', color='blue')
plt.plot(df['density'], df['kruskal'], label='kruskal', color='red')
# Add labels and title
plt.xlabel('Density')
plt.ylabel('Comparison')
plt.title("Prim's Algorithm: Average Weight vs. Density")

# Show the plot
plt.grid(True)
plt.legend()
plt.show()
