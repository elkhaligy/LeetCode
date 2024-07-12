def minOperations(nums: list[int]) -> int:

    min_steps = 0
    prev_num = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] == prev_num or nums[i] < prev_num:
            old_num = nums[i]
            nums[i] = prev_num + 1
            min_steps += nums[i] - old_num
        prev_num = nums[i]
    
    return min_steps
     

print(minOperations(nums = [1,1,1]))
