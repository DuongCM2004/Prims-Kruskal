import sys
import networkx as nx

def min_key(vertices, key, mst_set):
    min_value = sys.maxsize
    min_index = None

    for v in range(vertices):
        if key[v] < min_value and not mst_set[v]:
            min_value = key[v]
            min_index = v
    if min_index is not None:
        return min_index
    else:
        return -1  # Or any other suitable sentinel value


def prim(adj_matrix):
    vertices = len(adj_matrix)
    # Initialize lists to store MST and key values
    mst = [None] * vertices
    key = [sys.maxsize] * vertices
    mst_set = [False] * vertices

    # Start from the first vertex
    key[0] = 0
    mst[0] = -1
    result = []

    for _ in range(vertices):
        # Choose the minimum key vertex not yet in MST
        u = min_key(vertices, key, mst_set)
        mst_set[u] = True

        # Update key values and MST for adjacent vertices
        for v in range(vertices):
            if adj_matrix[u][v] and not mst_set[v] and adj_matrix[u][v] < key[v]:
                mst[v] = u
                key[v] = adj_matrix[u][v]

    for i in range(len(mst)):
        result.append([mst[i], i, key[i]])
    return result

def prim_mst(graph):
    # Initialize an empty MST
    mst = nx.Graph()

    # Choose an arbitrary starting vertex
    start_vertex = list(graph.nodes())[0]

    # Initialize sets for visited and unvisited vertices
    visited = {start_vertex}
    unvisited = set(graph.nodes()) - visited

    # Repeat until all vertices are visited
    while unvisited:
        min_edge = None
        min_weight = float('inf')

        # Find the minimum weight edge connecting a visited vertex to an unvisited vertex
        for u in visited:
            for v in unvisited:
                if graph.has_edge(u, v):
                    weight = graph[u][v]['weight']
                    if weight < min_weight:
                        min_weight = weight
                        min_edge = (u, v)

        # Add the minimum weight edge to the MST
        if min_edge:
            u, v = min_edge
            mst.add_edge(u, v, weight=min_weight)
            # Update visited and unvisited sets
            visited.add(v)
            unvisited.remove(v)

    return mst