def maxSatisfied_bruteforce_TLE(customers: list[int], grumpy: list[int], minutes: int) -> int:
    n = len(customers)
    answer = 0
    
    for i in range(n):
        if grumpy[i] == 0:
            answer += customers[i]
            customers[i] = 0

    current_sum = 0
    max_sum = 0
    for i in range(0, n):
        for j in range(i, i + minutes):
            if j >= n:
                break
            current_sum += customers[j]
        max_sum = max(current_sum, max_sum)
        current_sum = 0
    
    answer += max_sum
    return answer

def maxSatisfied_sliding_window_opt(customers: list[int], grumpy: list[int], minutes: int) -> int:
    n = len(customers)
    answer = 0
    
    for i in range(n):
        if grumpy[i] == 0:
            answer += customers[i]
            customers[i] = 0

    left, right = 0, 0
    current_sum = 0
    max_sum = 0

    while right < n:
        current_sum += customers[right]

        if right - left >= minutes:
            current_sum -= customers[left]
            left += 1

        max_sum = max(max_sum, current_sum)    
        right += 1

    answer += max_sum
    return answer

print(maxSatisfied_sliding_window_opt(customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3))