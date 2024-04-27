import random
import numpy as np
import networkx as nx

from Compare_prims_and_Kruskal import density


# Generate dense graph as adjacency matrix
def generate_dense_graph(num_vertices, max_weight=10):
    graph = [[0] * num_vertices for _ in range(num_vertices)]
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            weight = random.randint(1, max_weight)
            graph[i][j] = weight
            graph[j][i] = weight
    return graph

# Generate dense graph as graph
def generate_weighted_dense_graph(n_nodes):
    dense_graph = nx.Graph()

    # Add nodes to the graph
    dense_graph.add_nodes_from(range(n_nodes))

    # Add edges to the graph with random weights
    for i in range(n_nodes):
        for j in range(i+1, n_nodes):
            dense_graph.add_edge(i, j, weight=random.randint(1, 10))

    return dense_graph

# Generate sparse graph as adjacency matrix
def sparse_adjacency_matrix(num_nodes, num_edges, weight_range=(1, 10)):
    # Create an empty adjacency matrix
    adjacency_matrix = np.zeros((num_nodes, num_nodes))

    # Generate random edges with weights
    edges = set()
    while len(edges) < num_edges:
        node1 = np.random.randint(0, num_nodes)
        node2 = np.random.randint(0, num_nodes)
        weight = np.random.randint(weight_range[0], weight_range[1] + 1)
        if node1 != node2 and (node1, node2) not in edges and (node2, node1) not in edges:
            edges.add((node1, node2))
            adjacency_matrix[node1][node2] = weight
            adjacency_matrix[node2][node1] = weight  # Assuming an undirected graph

    return adjacency_matrix

# Generate sparse graph as graph
def generate_weighted_sparse_graph(num_nodes, num_edges, weight_range=(1, 10)):
    # Create an empty graph
    G = nx.Graph()

    # Add nodes
    G.add_nodes_from(range(num_nodes))

    # Add edges randomly with weights
    edge_count = 0
    while edge_count < num_edges:
        node1 = random.randint(0, num_nodes - 1)
        node2 = random.randint(0, num_nodes - 1)
        weight = random.randint(weight_range[0], weight_range[1])
        if node1 != node2 and not G.has_edge(node1, node2):
            G.add_edge(node1, node2, weight=weight)
            edge_count += 1

    return G

def generate_graph_with_density(num_node, density, weight_range = (1, 10)):
    # Create an empty graph
    actual_edges = 0
    G = nx.Graph()
    # Add nodes
    G.add_nodes_from(range(num_node))
    # calculate the num_edge due to density
    max_edges = (num_node * (num_node - 1)) / 2
    if density == 0:
        actual_edges = num_node - 1
    elif density > 1:
        print('Error')
    else:
        actual_edges = int(density * max_edges)
    # Add edges randomly with weights
    edge_count = 0
    while edge_count < actual_edges:
        node1 = np.random.randint(0, num_node - 1)
        node2 = np.random.randint(0, num_node - 1)
        weight = random.randint(weight_range[0], weight_range[1])
        if node1 != node2 and not G.has_edge(node1, node2):
            G.add_edge(node1, node2, weight=weight)
            edge_count += 1
    return G

def generate_graph(num_vertices, density, max_weight=10):
    # Initialize an empty adjacency matrix
    graph = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    # Calculate the maximum number of edges possible based on density
    max_edges = (num_vertices * (num_vertices - 1)) // 2
    num_edges = int(density * max_edges)

    # Randomly assign edges based on density
    edge_count = 0
    while edge_count < num_edges:
        # Randomly select two distinct vertices
        vertex1 = random.randint(0, num_vertices - 1)
        vertex2 = random.randint(0, num_vertices - 1)
        weight = random.randint(1, max_weight)
        if vertex1 != vertex2 and graph[vertex1][vertex2] == 0:
            graph[vertex1][vertex2] = weight
            graph[vertex2][vertex1] = weight
            edge_count += 1

    return graph

def generate_negative_weighted_graph(num_vertices, density, percentage, max_weight=10, max_negative_weight= -10):
    # Initialize an empty adjacency matrix
    graph = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    # Calculate the maximum number of edges possible based on density
    max_edges = (num_vertices * (num_vertices - 1)) // 2
    num_edges = int(density * max_edges)

    num_negative_edges = int(percentage * num_edges)
    num_positive_edges = num_edges - num_negative_edges

    # Randomly assign positive edges
    edge_count = 0
    while edge_count < num_positive_edges:
        vertex1 = random.randint(0, num_vertices - 1)
        vertex2 = random.randint(0, num_vertices - 1)
        weight = random.randint(1, max_weight)
        if vertex1 != vertex2 and graph[vertex1][vertex2] == 0:
            graph[vertex1][vertex2] = weight
            graph[vertex2][vertex1] = weight
            edge_count += 1

    # Randomly assign negative edges
    edge_negative_count = 0
    while edge_negative_count < num_negative_edges:
        vertex1 = random.randint(0, num_vertices - 1)
        vertex2 = random.randint(0, num_vertices - 1)
        weight = random.randint(max_negative_weight, -1)
        if vertex1 != vertex2 and graph[vertex1][vertex2] == 0:
            graph[vertex1][vertex2] = weight
            graph[vertex2][vertex1] = weight
            edge_negative_count += 1

    return graph