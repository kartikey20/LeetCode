def solve(n, edges):
    graph = [[] for _ in range(n)]
    for x in edges:
        graph[x[0]].append(x[1])
    print(graph)
