from bisect import bisect_left, bisect_right
arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]


# def negate(n):
#     return -1*n


# arr = list(map(negate, arr))

sub = []
for val in arr:
    pos = bisect_left(sub, val)
    print(pos)
    if pos == len(sub):
        sub.append(val)
    else:
        sub[pos] = val
print(sub)
