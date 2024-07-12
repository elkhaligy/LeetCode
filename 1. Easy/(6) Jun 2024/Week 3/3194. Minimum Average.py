def minimumAverage(nums: list[int]) -> float:
    nums.sort()
    average = float('inf')

    left, right = 0, len(nums) - 1
    while left < right:
        average = min(average, (nums[left] + nums[right]) / 2)
        right -= 1
        left += 1
    return average