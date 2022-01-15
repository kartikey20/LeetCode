lst = []
N = int(input())
for _ in range(N):
    arr = list(input())
    lst.append(arr)


def find_prefix(arr):
    for i in range(len(arr)):
        indices = set()
        count = 0
        s = arr[i][0]
        for j in range(len(arr)):
            if arr[j][0] == s:
                count += 1
                indices.add(j)
                if count == 2:
                    return [s, indices]
    return ["", set()]


def dfs(arr, count):
    prefix, prefix_indices = find_prefix(arr)
    if len(prefix_indices) == 0:
        return count
    else:
        new_arr = [arr[i] for i in range(len(arr)) if i not in prefix_indices]
        new_arr.append(prefix)
        return dfs(new_arr, count+1)


print(dfs(lst, 0))
