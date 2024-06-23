def minOperations(nums: list[int]) -> int:
    answer = 0

    for i in range(len(nums)):
        if nums[i] == 0 and i >= len(nums) - 2:
            return -1
        if nums[i] == 0:
            nums[i] ^= 1
            nums[i + 1] ^= 1
            nums[i + 2] ^= 1
            answer += 1

    
    return answer

print(minOperations(nums = [0,1,1,1,0,0]))