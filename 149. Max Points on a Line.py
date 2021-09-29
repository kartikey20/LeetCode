import collections
from math import gcd


def maxPoints(self, points):
    answer = 0
    for p in points:
        pctr = 0
        ctr = collections.Counter()
        for q in points:
            x, y = q[0] - p[0], q[1] - p[1]
            pctr += x == y == 0
            g = gcd(x, y)
            ctr[(y/g, x/g) if x else 'inf'] += 1
        ctr['inf'] -= pctr
        answer = max(answer, pctr + max(ctr.values()))
    return answer


print(maxPoints(maxPoints, [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
