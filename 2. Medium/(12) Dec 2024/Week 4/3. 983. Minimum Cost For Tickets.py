def mincostTickets(days: list[int], costs: list[int]) -> int:
    dp = [float('inf')] * (days[-1] + 1)
    dp[0] = 0
    daysIndex = 0
    for i in range(1, days[-1] + 1):
        if i < days[daysIndex]:
            dp[i] = dp[i - 1]
        else:
            daysIndex += 1
            dp[i] = min(dp[i - 1] + costs[0], dp[max(0, i - 7)] + costs[1], dp[max(0, i - 30)] + costs[2])

    return dp[-1]

print(mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15]))