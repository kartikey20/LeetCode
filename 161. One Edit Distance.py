def solve(s, t):
    ns, nt = len(s), len(t)
    temp = s
    if nt - ns > 1:
        return False

    if ns > nt:
        temp = s
        s = t
        t = temp
        ns, nt = nt, ns

    for i in range(ns):
        if s[i] != t[i]:
            if ns == nt:
                return s[i+1:] == t[i+1:]
            else:
                return s[i:] == t[i+1:]
    return ns + 1 == nt


print(solve('acb', 'ab'))
