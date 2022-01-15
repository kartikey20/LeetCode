# @before-stub-for-debug-begin
# @before-stub-for-debug-end
#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start


class NumArray:

    def __init__(self, nums: List[int]):
        self.res = []
        self.n = len(nums)
        self.arr = nums
        self.bit = [0 for _ in range(self.n+1)]
        for index in range(1+self.n+1):
            self.update(index, self.arr[index])

    def update(self, index, value):
        while index < self.n:
            self.bit[index] += value
            index += index & -index

    def get_sum(self, index):
        ans = 0
        while index > 0:
            ans += self.bit[index]
            index -= index & -index
        return ans

    def get_range_sum(self, left, right):
        res = self.get_sum(right, self.bit) - self.get_sum(left-1, self.bit)
        return res

    def sumRange(self, left: int, right: int) -> int:
        return self.get_range_sum(left, right)

        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # param_1 = obj.sumRange(left,right)
        # @lc code=end
