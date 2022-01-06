# @before-stub-for-debug-begin
from python3problem672 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=672 lang=python3
#
# [672] Bulb Switcher II
#

# @lc code=start


class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        def opposite(x):
            if x is True:
                return False
            if x is False:
                return True
        bulbs = tuple([True for _ in range(n)])
        visited = set()

        def bfs(start):
            queue = [[start, 0]]
            visited.add(start)
            for elem in queue:
                node, count = elem
                # button 1
                button_1_order = tuple([opposite(i) for i in node])
                if button_1_order not in visited:
                    visited.add(button_1_order)
                    button_1_count = count + 1
                    queue.append([button_1_order, button_1_count])
                    if button_1_count == presses:
                        return len(queue)
                # button 2
                button_2_order = tuple([opposite(node[i]) for i in range(len(node)) if i % 2 == 0])
                if button_2_order not in visited:
                    visited.add(button_2_order)
                    button_2_count = count + 1
                    queue.append([button_2_order, button_2_count])
                    if button_2_count == presses:
                        return len(queue)
                # button 3
                button_3_order = tuple([opposite(node[i]) for i in range(len(node)) if i % 2 != 0])
                if button_3_order not in visited:
                    visited.add(button_3_order)
                    button_3_count = count+1
                    queue.append([button_3_order, button_3_count])
                    if button_3_count == presses:
                        return len(queue)
                # button 4
                button_4_order = tuple([opposite(node[i]) for i in range(0, len(node), (3*i)+1)])
                if button_4_order not in visited:
                    visited.add(button_4_order)
                    button_4_count = count + 1
                    queue.append([button_4_order, button_4_count])
                    if button_4_count == presses:
                        return len(queue)
        return bfs(bulbs)

# @lc code=end
