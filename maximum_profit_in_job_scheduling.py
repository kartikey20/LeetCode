from collections import defaultdict


def jobScheduling(startTime, endTime, profit):
    jobs = []
    for i in range(len(startTime)):
        jobs.append((startTime[i], endTime[i], profit[i]))
    ans = 0
    jobs.sort(key=lambda x: x[1])
    dic = defaultdict(int)
    for job in jobs:
        max_profit_till_start_time = dic[job[0]]
        ans = max(ans, max_profit_till_start_time + job[2])
        dic[job[1]] = ans
    return ans


print(jobScheduling([1, 2, 3, 4, 6],
                    [3, 5, 10, 6, 9],
                    [20, 20, 100, 70, 60]))
