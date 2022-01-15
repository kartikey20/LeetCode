# @before-stub-for-debug-begin
# from python3problem752 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#
from copy import deepcopy
# @lc code=start


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_set = set()
        for x in deadends:               # O(4*N)
            deadends_set.add(tuple([int(i) for i in x]))

        target_lst = [int(i) for i in target]  # O(N)
        # print(target_lst)
        visited = set()
        arr = [0 for _ in range(4)]  # O(4)

        def bfs(start):
            steps = float('inf')
            queue = [[start, 0]]
            visited.add(tuple(start))
            for elem in queue:
                node, count = elem
                # print(node)
                for i in range(4):  # O(2*4)
                    new_arr = deepcopy(node)
                    new_arr_rev = deepcopy(node)
                    new_arr[i] += 1
                    if new_arr_rev[i] == 0:
                        new_arr_rev[i] = 9
                    else:
                        new_arr_rev[i] -= 1
                    new_rev_tuple = tuple(new_arr_rev)

                    if new_arr[i] <= 9:
                        new_tuple = tuple(new_arr)
                        if new_tuple not in visited and new_tuple not in deadends:
                            if new_arr == target_lst:
                                print(count + 1)
                            else:
                                visited.add(new_tuple)
                                queue.append([new_arr, count + 1])

                    if new_rev_tuple not in visited and new_rev_tuple not in deadends:
                        if new_arr_rev == target_lst:
                            print(count + 1)
                        else:
                            visited.add(new_rev_tuple)
                            queue.append([new_arr_rev, count + 1])
            # print(visited)
            # return steps

        bfs(arr)
        print(len(visited))


A = Solution()
A.openLock(["8888"], "0003")
# @lc code=end
