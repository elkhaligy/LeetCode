def maximumHappinessSum(happiness: list[int], k: int) -> int:
    happiness.sort(reverse=True)
    ans = 0
    for i in range(k):
        if happiness[i] > 0:
            happiness[i] -= i
            if happiness[i] < 0:
                happiness[i] = 0
            
        ans += happiness[i]
    
    return ans

def maximumHappinessSum_Time_Exceed(happiness: list[int], k: int) -> int:
    happiness.sort(reverse=True)
    ans = 0
    for i in range(k):
        ans += happiness[i]
        for k in range(i + 1, len(happiness)):
            if happiness[k] > 0:
                happiness[k] -= 1

    print(ans)
maximumHappinessSum( [12,1,42], 3)


