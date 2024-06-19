def minSubArrayLen(target: int, nums: list[int]) -> int:
    n = len(nums)
    current_sum = 0
    left, right = 0, 0
    answer = float('infinity')

    while right < n:
        current_sum += nums[right]

        while current_sum >= target:
            answer = min(answer, right - left + 1)
            current_sum -= nums[left]
            left += 1
        right += 1

    return 0 if answer == float('inf') else answer
print(minSubArrayLen(target = 1, nums = [2]))
