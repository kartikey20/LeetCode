from collections import defaultdict
nums = [4, 5, 0, -2, -3, 1]
K = 5
curr_sum = 0
prefix_mod = defaultdict(list)
prefix_mod[0] = [-1]
n = len(nums)
res = []
for i in range(n):
    curr_sum += nums[i]
    start_lst = prefix_mod[curr_sum % K]
    for x in start_lst:
        res.append([x+1, i])
    start_lst2 = prefix_mod[curr_sum % K]
    start_lst2.append(i)
    prefix_mod[curr_sum % K] = start_lst2

print(res)
