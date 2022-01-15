from itertools import combinations
from math import gcd

N = int(input())
A = []
for i in range(N):
    elem = int(input())
    A.append(elem)

B = []
for i in range(N):
    elem = int(input())
    B.append(elem)


def check_magical(tup):
    for i in range(len(tup)-1):
        if gcd(tup[i], tup[i+1]) == min(tup[i], tup[i+1]):
            continue
        else:
            return False
    return True


def beauty(tup):
    res = 0
    print(tup)
    for x in tup:
        res ^= B[x]
    return res


max_beauty = 0
for i in range(1, N):
    for comb in combinations(A, i):
        if check_magical(comb):
            max_beauty = max(max_beauty, beauty(list(comb)))

print(max_beauty)
