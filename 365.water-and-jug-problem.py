#
# @lc app=leetcode id=365 lang=python3
#
# [365] Water and Jug Problem
#

# @lc code=start
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        water_in_jugs = set()
        if jug1Capacity > jug2Capacity:
            jug1Capacity, jug2Capacity = jug2Capacity, jug1Capacity
        water_in_jugs.add([jug1Capacity, jug2Capacity])
        while not [jug1Capacity, jug2Capacity] in water_in_jugs:

            # @lc code=end
