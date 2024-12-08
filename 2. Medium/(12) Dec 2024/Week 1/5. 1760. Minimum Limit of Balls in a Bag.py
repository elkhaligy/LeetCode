import math

def minimumSize(nums: list[int], maxOperations: int) -> int:
    def testDivision(maxBagSize: int) -> bool:
        operationsNeeded = 0
        for num in nums:
            if num > maxBagSize:
                operationsNeeded += (math.ceil(num / maxBagSize) - 1)
        return operationsNeeded <= maxOperations
    
    left = 1 
    right = max(nums)
    while left <= right:
        mid = left + (right - left) // 2
        if testDivision(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer

# 2 -> 1, 1
# 4 -> 2, 2 -> 1,1   , 1,1

print(minimumSize(nums = [2,4,8,2], maxOperations = 4))
