from collections import Counter
def missingNumber(nums: list[int]) -> int:
    occu_dict = Counter(nums)

    for i in range(1, len(nums) + 1):
        if i not in occu_dict:
            return i
def missingNumber_sol2(nums):
    xoring_1 = 0
    for i in range(0, len(nums)):
        xoring_1 ^= nums[i]
    
    for i in range(0, len(nums) + 1):
        xoring_1 ^= i
    
    return xoring_1

# 1 2 3
print(missingNumber_sol2( nums = [1, 2, 3]))