# Time - complexity on dense graph as graph
import timeit
import Prims
import graph

def worst_case_prims(vertice):
    avg_time_worst_case = []
    index = []
    density = 1
    for i in range (5, vertice):
        num = 50
        time_vertice = []
        for j in range(1, num):
          start = timeit.default_timer()
          num_nodes = i
          graph_worst_case = graph.generate_graph(num_nodes, density)
          mst = Prims.prim(graph_worst_case)
          stop = timeit.default_timer()
          expe_time = stop - start
          time_vertice.append(expe_time)
        avg_time_worst_case.append(sum(time_vertice)/len(time_vertice))
        index.append(i)
    return avg_time_worst_case, index

def best_case_prims(vertice):
    avg_time_best_case = []
    index = []
    density = 0
    for i in range(5, vertice):
        num = 50
        time_vertice = []
        for j in range(1, num):
          start = timeit.default_timer()
          num_nodes = i
          graph_best_case = graph.generate_graph(num_nodes, density)
          mst = Prims.prim(graph_best_case)
          stop = timeit.default_timer()
          expe_time = stop - start
          time_vertice.append(expe_time)
        avg_time_best_case.append(sum(time_vertice)/len(time_vertice))
        index.append(i)

    return avg_time_best_case, index

def avg_case_prims(vertice):
    avg_time_avg_case = []
    index = []
    density = 0.5
    for i in range(5, vertice):
        num = 50
        time_vertice = []
        for j in range(1, num):
          start = timeit.default_timer()
          num_nodes = i
          graph_avg_case = graph.generate_graph(num_nodes, density)
          mst = Prims.prim(graph_avg_case)
          stop = timeit.default_timer()
          expe_time = stop - start
          time_vertice.append(expe_time)
        avg_time_avg_case.append(sum(time_vertice)/len(time_vertice))
        index.append(i)

    return avg_time_avg_case, index
