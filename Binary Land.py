N, Q = map(int, input().split())
queries = []
for _ in range(Q):
    queries.append(list(map(int, input().split())))


def solve(n, q, queries):
    visited = [[False for _ in range(n)] for _ in range(n)]
    paths = []
    matrix = []
    res = []

    def valid(row, col):
        return 0 <= row < n and 0 <= col < n

    def dfs(row, col, path, end):
        visited[row][col] = True
        if valid(row+1, col) and not visited[row+1][col] and queries[row+1][col] == queries[row][col]:
            dfs(row+1, col, path[:])
        if valid(row+1, col-1) and not visited[row+1][col-1] and queries[row+1][col-1] == queries[row][col]:
            dfs(row+1, col-1, path[:])
        if valid(row, col+1) and not visited[row][col+1] and queries[row][col+1] == queries[row][col]:
            dfs(row, col+1, path[:])

    for query in queries:
        q = query.split()
        if q[0] == 'add':
            matrix.append(q[1])

        elif q[0] == 'path':
            dfs(int(q[1]), int(q[2]), [])
            res.append(len(paths))
            paths = []
            visited = [[False for _ in range(n)] for _ in range(n)]

        elif q[0] == 'remove':
            matrix.pop()
