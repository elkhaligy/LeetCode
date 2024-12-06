def maxCount(banned: list[int], n: int, maxSum: int) -> int:
    setBanned = set(banned)
    answer = []
    currSum = 0

    for num in range(1, n + 1):
        if num not in setBanned:
            answer.append(num)
            currSum += num
            if currSum > maxSum:
                return len(answer) - 1
    
    return len(answer)


print(maxCount(banned = [1,6,5], n = 5, maxSum = 6))
