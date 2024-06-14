# n amount
def coin(n: int):
    # ways: index: amount, value: number of ways
    ways = [0] * (n + 1)
    ways[0] = 1

    for coin in coins:
        for i in range(coin, n + 1):
            ways[i] += ways[i - coin]
    
    return ways

coins = [1, 2, 5]

print(coin(5))
