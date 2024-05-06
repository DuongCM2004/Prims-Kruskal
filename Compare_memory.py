import graph
import Memory_Analyzer as ma
import matplotlib.pyplot as plt
import pandas as pd


numnodes = 15
density = 100
index = []
memory_write_prims = []
memory_write_kruskal = []
memory_read_prims = []
memory_read_kruskal = []

# Running graph according to density
for i in range(20, density):
    calculate_density = i/100
    ge_graph = graph.generate_graph(numnodes, calculate_density)

    # Store Prims
    mst, read_prims, write_prims = ma.prim(ge_graph)
    memory_read_prims.append(read_prims)
    memory_write_prims.append(write_prims)

    # Store Kruskal
    mst1, read_kruskal, write_kruskal = ma.kruskal(ge_graph)
    memory_read_kruskal.append(read_kruskal)
    memory_write_kruskal.append(write_kruskal)
    index.append(calculate_density)

df = pd.DataFrame({
    'Density': index,
    'Memory_Write_Prims': memory_write_prims,
    'Memory_Write_Kruskal': memory_write_kruskal,
    'Memory_Read_Prims': memory_read_prims,
    'Memory_Read_Kruskal': memory_read_kruskal
})

plt.scatter(df['Density'], df['Memory_Write_Prims'])
plt.scatter(df['Density'], df['Memory_Write_Kruskal'])
plt.title('Compare Prims and Kruskal: Write memory')
plt.xlabel('Density')
plt.ylabel('Memory')
plt.legend(['Prims', 'Kruskal'])
plt.grid(True)
plt.show()

plt.scatter(df['Density'], df['Memory_Read_Prims'])
plt.scatter(df['Density'], df['Memory_Read_Kruskal'])
plt.title('Compare Prims and Kruskal: Read_memory')
plt.xlabel('Density')
plt.ylabel('Memory')
plt.legend(['Prims', 'Kruskal'])
plt.grid(True)
plt.show()

