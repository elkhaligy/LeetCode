import heapq

def getFinalState(nums: list[int], k: int, multiplier: int) -> list[int]:
    
    while k:
        minIndex = nums.index(min(nums))
        nums[minIndex] = nums[minIndex] * multiplier
        k -= 1
    
    return nums

print(getFinalState(nums = [2,1,3,5,6], k = 5, multiplier = 2))
