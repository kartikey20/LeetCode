#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        count = 0
        print(citations)
        for i, j in enumerate(citations):
            print(i, j)
            if i < j:
                count += 1
        return count


# @lc code=end
