def maxSubArray(self, nums: List[int]) -> int:
    maxi = 0
    for i in combinations(nums, len(nums)):
        maxi = max(maxi, sum(i))
    return maxi
