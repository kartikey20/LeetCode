from collections import defaultdict


def alienDictionary(words):
    graph = defaultdict(set)
    for word in words:
        for i in range(len(word)-1):
            graph[word[i]].add(word[i+1])

    print(graph)
# e < r


alienDictionary(["wrt", "wrf", "er", "ett", "rftt"])
