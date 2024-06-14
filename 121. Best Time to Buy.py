def maxProfit(prices: list[int]) -> int:
    buy = prices[0]
    sol = 0
    for price in prices[1:]:
        if price < buy:
            buy = price
        else:
            sol = max(sol, price - buy)
    
    return sol

print(maxProfit(prices = [7,1,5,3,6,4]))