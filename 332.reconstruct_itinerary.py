#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#
from collections import defaultdict
# @lc code=start


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dic = defaultdict(bool, tickets)
        curr = ""
        while dic[curr]:

            # @lc code=end
