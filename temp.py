def nextMultiple(n, k):
    return n + (k - n % k) if n % k else n

print(nextMultiple(7,7))