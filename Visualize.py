import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
def visualize_adjacency_matrix(adjacency_matrix):
    # Convert the adjacency matrix to a NetworkX graph
    G = nx.from_numpy_array(np.array(adjacency_matrix))

    # Create a dictionary to store edge labels
    edge_labels = {(i, j): adjacency_matrix[i][j] for i in range(len(adjacency_matrix)) for j in
                   range(len(adjacency_matrix[i])) if adjacency_matrix[i][j] != 0}

    # Draw the graph
    plt.figure(figsize=(6, 6))
    pos = nx.spring_layout(G)  # Position nodes using Fruchterman-Reingold force-directed algorithm
    nx.draw(G, pos, with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)  # Draw edge labels
    # Show the graph
    plt.show()

def visualize_mst(mst_sparse, key):
    G = nx.Graph()

    for i in range(1, len(mst_sparse)):
        G.add_edge(i, mst_sparse[i])

    # Draw the graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=12, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(i, mst_sparse[i]): key[i] for i in range(1, len(mst_sparse))})
    plt.title("Minimum Spanning Tree (MST)")
    plt.show()

def visualize_mst_list(mst_edges):
    G = nx.Graph()

    # Add edges to the graph
    for edge in mst_edges:
        G.add_edge(edge[0], edge[1])

    # Draw the graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=12, font_weight='bold')

    # Add edge labels
    edge_labels = {(edge[0], edge[1]): edge[2] for edge in mst_edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Minimum Spanning Tree (MST)")
    plt.show()