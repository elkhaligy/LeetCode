def minimumOperations(nums: list[int]) -> int:
    answer = 0

    for num in nums:
        if (num + 1) % 3 == 0:
            answer += 1
        else:
            answer += num % 3

    
    return answer


print(minimumOperations(nums = [1,2,3,4]))