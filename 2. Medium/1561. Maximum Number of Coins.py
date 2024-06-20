def maxCoins(piles: list[int]) -> int:
    n = len(piles)
    piles.sort()
    ans = 0
    for i in range(n - 2, len(piles) // 3 - 1, -2):
        ans += piles[i]

    return ans

def maxCoins_oN(piles: list[int]) -> int:
    iterations = len(piles) // 3
    ans = 0
    freq = [0] * (10000 + 1)

    for item in piles:
        freq[item] += 1

    cur_num = len(freq) - 1
    my_turn = False
    while iterations:
        if freq[cur_num] > 0:

            if not my_turn:
                my_turn = True
            else:
                ans += cur_num
                my_turn = False
                iterations -= 1
            freq[cur_num] -= 1

        else:
            cur_num -= 1

    return ans

print(maxCoins_oN(piles = [2,4,1,2,7,8]))
