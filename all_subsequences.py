from itertools import combinations


def all_subsequences(arr):
    res = set()
    possibles = []
    for i in range(1, len(arr) + 1):
        for comb in combinations(arr, i):
            res.add(comb)

    for x in res:
        if sum(x) == target:
            possibles.append(x)
