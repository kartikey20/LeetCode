from itertools import groupby
from copy import deepcopy
# import string


def group_shifted_string(strings):

    def shift(first, second):
        for i in range(len(first)):
            if abs(
                    ord(first[i]) - ord(second[i])) or (
                    first[i] == 'a' and second[i] == 'z') or (
                    first[i] == 'z' and second[i] == 'a'):
                continue
            else:
                return False
        return True

    def dfs(start, n, list, visited_set, s_set):
        visited_set.add(start)
        s_set.add()
        for i in range(n):
            if list[i] not in visited_set:
                if shift(start, list[i]):
                    dfs(list[i], n, list, visited_set, s_set)

    strings.sort(key=len)
    for i, group in groupby(strings, key=len):
        print(i, list(group))


print(group_shifted_string(["acd", "dfg", "wyz", "yab", "mop",
                            "bdfh", "a", "x", "moqs"])
      )
