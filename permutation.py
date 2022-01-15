N = int(input())
K = int(input())
arr = []

for i in range(N):
    elem = int(input())
    arr.append(elem)

    def next_permutation(a):
        i = len(a) - 2
        while not (i < 0 or a[i] < a[i+1]):
            i -= 1
        if i < 0:
            return False

        j = len(a) - 1
        while not (a[j] > a[i]):
            j -= 1
        a[i], a[j] = a[j], a[i]
        a[i+1:] = reversed(a[i+1:])
        return a

    def check_good(perm):
        for i in range(1, len(perm)):
            if abs(perm[i] - perm[i-1]) != K:
                continue
            else:
                return False
        return True

    def dfs(arr, count):
        perm = next_permutation(arr)
        if perm is False:
            return count
        else:
            if check_good(perm):
                count += 1
            return dfs(perm, count)

    print(dfs(arr, 0))
