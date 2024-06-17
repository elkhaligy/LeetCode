def maxProfit_sol1(prices: list[int]) -> int:
    left = 0
    right = 1
    max_protif = 0
    
    while right < len(prices):
        if  prices[right] < prices[left]:
            left = right
    
        max_protif = max(max_protif, prices[right] - prices[left])
        right = right + 1

    return max_protif

def maxProfit_sol2(prices: list[int]) -> int:
    buy = prices[0]
    sol = 0
    for price in prices[1:]:
        if price < buy:
            buy = price
        else:
            sol = max(sol, price - buy)
    
    return sol


print(maxProfit_sol1(prices = [7,1,5,3,6,4]))