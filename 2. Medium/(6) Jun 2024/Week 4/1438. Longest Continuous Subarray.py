def longestSubarray_slidingwindow(nums: list[int], limit: int) -> int:
    # Sol is workin but needs optimizations
    left, right, longest = 0, 0, 0
    cur_sub = {}
    while right < len(nums):
        cur_sub[nums[right]] = cur_sub.get(nums[right], 0) + 1
        if abs(max(cur_sub) - min(cur_sub)) <= limit:
            longest = max(longest, right - left + 1)
        else:
            while abs(max(cur_sub) - min(cur_sub)) > limit:
                cur_sub[nums[left]] -= 1
                if cur_sub[nums[left]] == 0:
                    cur_sub.pop(nums[left])
                left += 1
        right += 1
    return longest
print(longestSubarray_slidingwindow(nums = [1,5,6,7,8,10,6,5,6], limit = 4))
