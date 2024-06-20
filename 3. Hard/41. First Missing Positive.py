def firstMissingPositive_extra_space(nums: list[int]) -> int:
    if len(nums) == 1:
        if nums[0] > 1:
            return 1
        elif nums[0] <= 0:
            return 1
        else:
            return 2

    tmp = set()
    for num in nums:
        if num > 0:
            tmp.add(num)
            
    if len(tmp) == 0:
        return 1

    for num in range(1, min(tmp)):
        if num not in tmp:
            return num
    
    for num in range(min(tmp), max(tmp)):
        if num not in tmp:
            return num
    
    return max(tmp) + 1

def firstMissingPositive_constant_space(nums: list[int]) -> int:
    if len(nums) == 1:
        if nums[0] > 1:
            return 1
        elif nums[0] <= 0:
            return 1
        else:
            return 2

    tmp = set()
    for num in nums:
        if num > 0:
            tmp.add(num)
            
    if len(tmp) == 0:
        return 1

    for num in range(1, min(tmp)):
        if num not in tmp:
            return num
    
    for num in range(min(tmp), max(tmp)):
        if num not in tmp:
            return num
    
    return max(tmp) + 1

print(firstMissingPositive_extra_space(nums = [3,4,-1,1]))
