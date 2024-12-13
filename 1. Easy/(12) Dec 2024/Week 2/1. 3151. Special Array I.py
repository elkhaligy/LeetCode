def isArraySpecial(nums: list[int]) -> bool:
    if len(nums) == 1:
        return True
    
    prevNum = nums[0]
    for num in nums[1:]:
        if num & 1 == prevNum & 1:
            return False
        prevNum = num
        
    return True

print(isArraySpecial(nums = [4,3,1,6]))
