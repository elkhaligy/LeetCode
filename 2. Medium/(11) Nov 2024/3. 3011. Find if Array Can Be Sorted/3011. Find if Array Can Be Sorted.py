def canSortArray_n2(nums: list[int]) -> bool:
    n = len(nums)
    
    for i in range(n):
        for j in range(n - i - 1):
            if nums[j] <= nums[j + 1]:
                continue
            else:
                if bin(nums[j]).count("1") == bin(nums[j + 1]).count("1"):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                else:
                    return False
    return True