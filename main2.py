from bisect import bisect_left
global_set = set()


def binary_search(arr, v):
    i = bisect_left(arr, v)
    if 0 <= i < len(arr) and arr[i] == v and v not in global_set:
        global_set.add(v)
        return v
    else:
        return False


def differ_by_one(arr):
    res = []
    arr.sort()
    print(arr)
    for x in arr:
        print(x)
        left = binary_search(arr, x-1)
        right = binary_search(arr, x+1)
        print(left, right)
        if left or right:
            if left:
                res.append([x, left])
            else:
                res.append([x, right])
    print(global_set)
    return res


print(differ_by_one([11, 1, 8, 12, 14]))
