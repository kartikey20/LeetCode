def smooth(inlist, h):
    """
    This function performs a basic smoothing
    of inlist, returning the result.  The
    returned array (outlist) will have the same
    length (N) as inlist.  Each outlist[i] will
    be the average of all inlist[k] that satisfy
    i-h <= k <= i+h  and  0 <= k <= N-1.
    """

    outlist = []
    N = len(inlist)
    for i in range(N):
        s = 0
        length = 0
        for k in range(N):
            if i - h <= k <= i + h:
                s += inlist[k]
                length += 1
        outlist.append(s / length)
    return outlist

# Time Complexity: O(N^2)
# Space Complexity: O(N)
