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


print(longest_increasing_subsequence([3, 2, 1, 4, 7, 8, 9, 10]))
