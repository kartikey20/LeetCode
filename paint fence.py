from math import comb, perm


def paint_fence(n, k):
    # number of ways to paint n fences with k colores
    # f(n) = f(n-1)*k
    # number of ways to paint three consecutive fences with k colors
    # f(n) = f(n-3) * k-1
    # ans = f(n-1) *k - f(n-3)*k-1

    if n == 1:
        return k
    if n == 2:
        return k*k
    if k < 2:
        return 0
    if n == 3:
        return k * (k-1 + (k-1)*k)
    else:
        return paint_fence(n-1, k) * k - paint_fence(n-3, k) * (k-1)


print(paint_fence(3, 2))
