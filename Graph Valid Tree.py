def validTree(n, edges):
    # n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    # write your code here
    if len(edges) != n-1:
        return False

    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False for _ in range(n)]

    def bfs(start):
        queue = [start]
        visited[start] = True
        for node in queue:
            for child in graph[node]:
                if not visited[child]:
                    visited[child] = True
                    queue.append(child)
    bfs(0)
    for x in visited:
        if not x:
            return False
    return True


print(validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
