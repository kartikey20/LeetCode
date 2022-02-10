import bisect


def longest_increasing_subsequence(arr):
    sub = []
    for val in arr:
        pos = bisect.bisect_left(sub, val)
        if pos == len(sub):
            sub.append(val)
        else:
            sub[pos] = val
    print(sub)
    return len(sub)


def isSubseq(x, y):
    it = iter(y)
    print(list(it))
    return all(c in it for c in x)


print(isSubseq([1, 2], [3, 2, 1, 4, 7, 8, 9, 10]))

# print(longest_increasing_subsequence([3, 2, 1, 4, 7, 8, 9, 10]))
