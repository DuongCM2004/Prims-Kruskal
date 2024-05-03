import random
import numpy as np
import networkx as nx

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