from graphlib import TopologicalSorter


def alienOrder(words):
    # Build the graph
    graph = {}
    for word in words:
        for letter in word:
            graph[letter] = []
    for i in range(len(words) - 1):
        for j in range(len(words[i])):
            if words[i][j] != words[i + 1][j]:
                graph[words[i][j]].append(words[i + 1][j])
                break
    ts = TopologicalSorter(graph)
    res = list(ts.static_order())
    return ''.join(res[::-1]) if len(res) == len(graph) else ''
