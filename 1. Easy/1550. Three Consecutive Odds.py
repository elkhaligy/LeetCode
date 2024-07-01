def threeConsecutiveOdds(arr: list[int]) -> bool:
    odds_counter = 0
    max_odds = 0
    
    for num in arr:
        if num % 2 == 1:
            odds_counter += 1
            max_odds = max(max_odds, odds_counter)
        else:
            odds_counter = 0

    return max_odds >= 3

print(threeConsecutiveOdds(arr = [1,2,34,3,4,5,7,23,12]))