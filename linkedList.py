import itertools


def allSubArrays(xs):
    return list(itertools.combinations(xs, 5//2))


print(allSubArrays([1, 2, 3, 5, 6]))
