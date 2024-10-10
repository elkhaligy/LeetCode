def maxWidthRamp_sliding_window(nums: list[int]) -> int:
    n = len(nums)
    right_max = [0] * n

    right_max[-1] = nums[-1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], nums[i])

    left = 0
    right = 0
    max_width = 0

    # Sliding window
    while right < n:
        while left < right and nums[left] > right_max[right]:
            left += 1
        max_width = max(max_width, right - left)
        right += 1

    return max_width

print(maxWidthRamp_sliding_window(nums = [6,0,8,2,1,5]))