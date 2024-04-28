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

def kruskal(graph):
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

    while e < V - 1:
        u, v, w = edges[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            e += 1
            result.append([u, v, w])
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