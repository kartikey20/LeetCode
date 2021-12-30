#
# @lc app=leetcode id=690 lang=python3
#
# [690] Employee Importance
#

# @lc code=start
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

from collections import defaultdict


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        # print(employees.subordinates)

        def dfs(emp):
            graph[emp.id] = [emp.importance, emp.subordinates]
            # print(emp.id)
            for node in emp.subordinates:
                dfs(node)
        dfs(employees)
        print(graph)

        # @lc code=end
