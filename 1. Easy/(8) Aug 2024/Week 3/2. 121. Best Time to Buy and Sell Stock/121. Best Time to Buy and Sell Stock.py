def maxProfit_bruteforce(prices: list[int]) -> int:
    n = len(prices)
    profit = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            profit = max(prices[j] - prices[i])
    
    return profit

def maxProfit_dp_3pass(prices: list[int]) -> int:
    n = len(prices)
    profit = 0

    left_min = [float('inf')] * n
    right_max = [0] * n

    left_min[0] = prices[0]
    right_max[-1] = prices[-1]

    for i in range(1, n):
        left_min[i] = min(left_min[i - 1], prices[i])
    
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], prices[i])

    for i in range(1, n):
        profit = max(profit, right_max[i] - left_min[i - 1])
    #print(left_min, right_max)
    return profit

print(maxProfit_dp_3pass([7,1,5,3,6,4]))