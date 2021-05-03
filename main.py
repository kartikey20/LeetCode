import itertools


def solve(start, end):
    s = "123456789"
    res = []
    for i in range(9):
        for j in range(i+1, 10):
            x = int(s[i:j])
            if start <= x <= end:
                res.append(x)
    return sorted(res)


print(solve(0, 100))
