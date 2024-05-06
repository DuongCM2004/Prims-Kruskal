def kruskal(graph):
    memory_reads = 0
    memory_writes = 0

    def read_memory(num_reads=1):
        nonlocal memory_reads
        memory_reads += num_reads

    def write_memory(num_writes=1):
        nonlocal memory_writes
        memory_writes += num_writes

    def find(parent, i):
        read_memory()
        if parent[i] == i:
            return i
        return find(parent, parent[i])

    def union(parent, rank, x, y):
        xroot = find(parent, x)
        yroot = find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
            write_memory()
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
            write_memory()
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
            write_memory(2)

    V = len(graph)
    result = []

    # Sort all the edges in non-decreasing order of their weight
    edges = []
    for i in range(V):
        for j in range(i + 1, V):
            if graph[i][j] != 0:
                edges.append((i, j, graph[i][j]))
    edges.sort(key=lambda x: x[2])

    parent = [i for i in range(V)]
    rank = [0] * V

    i = 0  # index variable, used for sorted edges
    e = 0  # index variable, used for result[]

    while e < V - 1 and i < len(edges):
        u, v, w = edges[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            e += 1
            result.append([u, v, w])
            union(parent, rank, x, y)

    return result, memory_reads, memory_writes

import sys

def prim(adj_matrix):
    memory_reads = 0
    memory_writes = 0

    def read_memory(num_reads=1):
        nonlocal memory_reads
        memory_reads += num_reads

    def write_memory(num_writes=1):
        nonlocal memory_writes
        memory_writes += num_writes

    def min_key(vertices, key, mst_set):
        min_val = sys.maxsize
        min_index = -1
        for v in range(vertices):
            read_memory(2)  # Reading key and mst_set
            if not mst_set[v] and key[v] < min_val:
                min_val = key[v]
                min_index = v
        return min_index

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
                write_memory(2)  # Writing to mst and key

    for i in range(1, len(mst)):
        result.append([mst[i], i, key[i]])
        read_memory(2)  # Reading mst and key

    return result, memory_reads, memory_writes

