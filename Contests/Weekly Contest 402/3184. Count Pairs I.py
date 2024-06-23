def countCompleteDayPairs(hours: list[int]) -> int:
    cnt = 0
    
    for i in range(len(hours) - 1):
        for j in range(i + 1, len(hours)):
            if (hours[i] + hours[j]) % 24 == 0:
                cnt += 1

    return cnt

print(countCompleteDayPairs(hours = [12,12,30,24,24]))