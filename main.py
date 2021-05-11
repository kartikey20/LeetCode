from collections import Counter


def solve(n):
    c = Counter(n)
    print(c['1'])


print(solve('00000000000000000000000000001011'))
