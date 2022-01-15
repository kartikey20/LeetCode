from copy import deepcopy
from math import floor
N = int(input())
M = int(input())
K = int(input())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b, c, d = map(int, input().split())
    graph[a].append([b, c, d])
    graph[b].append([a, c, d])
visited = [False for _ in range(N+1)]
res = [float('inf')]

# def bfs(start):
#     queue = [[start, 0, float('inf')]]
#     visited[start] = True
#     for elem in queue:
#         node, time, min_capacity = elem
#         if node == N:
#             # if time == 20:
#             #     return True
#             return time + K/min_capacity
#         for child in graph[node]:
#             if not visited[child[0]]:
#                 visited[child[0]] = True
#             queue.append([child[0], time+child[1], min(min_capacity, child[2])])


def dfs(node, visited, time, min_capacity):
    visited[node] = True
    if node == N:
        res[0] = min(res[0], floor(time + K/min_capacity))
    for child in graph[node]:
        if not visited[child[0]]:
            dfs(child[0], deepcopy(visited), time+child[1], min(min_capacity, child[2]))


print(dfs(1, deepcopy(visited), 0, float('inf')))
