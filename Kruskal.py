import sys

def min_key(vertices, key, mst_set):
    min_value = sys.maxsize
    min_index = None

    for v in range(vertices):
        if key[v] < min_value and not mst_set[v]:
            min_value = key[v]
            min_index = v

    return min_index

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(adj_matrix):
    num_vertices = len(adj_matrix)
    result = []

    # Sort all the edges in non-decreasing order of their weight
    edges = []
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if adj_matrix[i][j] != 0:
                edges.append((i, j, adj_matrix[i][j]))
    edges = sorted(edges, key=lambda x: x[2])

    parent = [i for i in range(num_vertices)]
    rank = [0] * num_vertices

    i = 0
    e = 0
    while e < num_vertices - 1 and i < len(edges):
        u, v, weight = edges[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            e += 1
            result.append((u, v, weight))
            union(parent, rank, x, y)

    return result

def kruskal_mst(graph):
    minimum_spanning_tree = []
    parent = {}
    rank = {}

    for vertex in list(graph.nodes()):
        parent[vertex] = vertex
        rank[vertex] = 0

    sorted_edges = sorted(list(graph.edges(data = True)), key=lambda edge: edge[2]['weight'])

    for edge in sorted_edges:
        src, dest, weight = edge
        src_root = find(parent, src)
        dest_root = find(parent, dest)

        if src_root != dest_root:
            minimum_spanning_tree.append(edge)
            union(parent, rank, src, dest)

    return minimum_spanning_tree