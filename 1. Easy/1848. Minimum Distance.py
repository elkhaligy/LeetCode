def getMinDistance(nums: list[int], target: int, start: int) -> int:
    min_val = float('inf')
    for i, num in enumerate(nums):
        if num == target:
            min_val = min(min_val, abs(i - start))
    
    return min_val

print(getMinDistance(nums = [1,2,3,4,5], target = 5, start = 3))
