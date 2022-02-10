from collections import defaultdict


def minSub(nums, k):
    prefix_sum = defaultdict(list)
    prefix_sum[0] = [-1]
    sums = 0
    for i in range(len(nums)):
        sums += nums[i]
        start_index = prefix_sum[sums-k]
        for x in start_index:
            print([x+1, i])
        start_index = prefix_sum[sums]
        start_index.append(i)
        prefix_sum[sums] = start_index


minSub([1, 2, 3, 4, 5, 6], 5)
