import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def visualize(adjacency_matrix, mst_edges1, mst_edges2):
    plt.figure(figsize = (10, 10))
    # Graph original
    plt.subplot(1, 3, 1)
    G = nx.from_numpy_array(np.array(adjacency_matrix))

    # Create a dictionary to store edge labels
    edge_labels = {(i, j): adjacency_matrix[i][j] for i in range(len(adjacency_matrix)) for j in
                   range(len(adjacency_matrix[i])) if adjacency_matrix[i][j] != 0}

    # Draw the graph
    pos = nx.spring_layout(G)  # Position nodes using Fruchterman-Reingold force-directed algorithm
    nx.draw(G, pos, with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)  # Draw edge labels
    # Show the graph
    plt.title("Original graph")


    # Draw the Prims graph
    plt.subplot(1, 3, 2)
    G1 = nx.Graph()

    # Add edges to the graph
    for edge in mst_edges1:
        G1.add_edge(edge[0], edge[1])

    # Draw the graph
    pos = nx.spring_layout(G1)
    nx.draw(G1, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=12, font_weight='bold')

    # Add edge labels
    edge_labels = {(edge[0], edge[1]): edge[2] for edge in mst_edges1}
    nx.draw_networkx_edge_labels(G1, pos, edge_labels=edge_labels)

    plt.title("Minimum Spanning Tree (Prims)")

    #Draw the Kruskal graph
    plt.subplot(1, 3, 3)
    G2 = nx.Graph()

    # Add edges to the graph
    for edge in mst_edges2:
        G2.add_edge(edge[0], edge[1])

    # Draw the graph
    pos = nx.spring_layout(G2)
    nx.draw(G2, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=12, font_weight='bold')

    # Add edge labels
    edge_labels = {(edge[0], edge[1]): edge[2] for edge in mst_edges2}
    nx.draw_networkx_edge_labels(G2, pos, edge_labels=edge_labels)

    plt.title("Minimum Spanning Tree (Kruskal)")
    plt.show()