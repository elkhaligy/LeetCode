

def coinChange(coins: list[int], amount: int) -> int:
    min_amoun_lst = [float('inf')] * (amount + 1)

    min_amoun_lst[0] = 0

    #print(min_amoun_lst)

    for cur_amount in range(1, amount + 1):
        #print(f"Current amount: {cur_amount} ->", end= " ")
        for coin in coins:
            if coin < cur_amount and min_amoun_lst[cur_amount - coin] != float('inf'):
                #print(f"Coin : {coin},", end=' ')
                min_amoun_lst[cur_amount] = min(min_amoun_lst[cur_amount], 1 + min_amoun_lst[cur_amount - coin])
            elif coin == cur_amount:
                #print(f"Coin : {coin},", end=' ')
                min_amoun_lst[cur_amount] = 1 
        #print()
    #print(min_amoun_lst)
    ans = min_amoun_lst[-1]
    return -1 if ans == float('inf') else ans
#
def coinChange_Sol2(coins: list[int], amount: int) -> int:
    min_ways = [float('inf') for _ in range(amount + 1)]
    min_ways[0] = 0
    for coin in coins:
        if len(min_ways) -1 >= coin:
            min_ways[coin] = 1
    for cur_amount in range(1, amount + 1):
        if min_ways[cur_amount] != 1:
            for coin in coins:
                if coin <= cur_amount:
                    min_ways[cur_amount] = min(1 + min_ways[cur_amount - coin], min_ways[cur_amount])
            
    return -1 if min_ways[-1] == float('inf') else min_ways[-1]



print(coinChange_Sol2( coins = [1,2,5], amount = 11))