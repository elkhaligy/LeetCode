def longestConsecutive_nlogn(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1
    nums.sort()
    ans = 0
    cur = 0
    start = 0
    end = 1
    while end != len(nums):
        if nums[start] == nums[end]:
            end += 1
            start += 1
        elif nums[end] == nums[start] + 1:
            cur += 1
            start += 1
            end += 1
        else:
            cur = 0
            end += 1
            start += 1
        ans = max(ans, cur)
    return ans + 1
def longestConsecutive_nlogn_sol2(nums: list[int]) -> int:
    nums = set(nums)
    nums.sort()
    ans = 1
    cur = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            cur += 1
            ans = max(cur, ans)
        else:
            cur = 1
    return ans

def longestConsecutive_n(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1
    nums = set(nums)
    longest = 1
    cur = 1
    for num in nums:
        if num - 1 in nums:
            cur = 1
            while num - 1 in nums:
                cur += 1
                num -= 1
        longest = max(longest, cur)
    return longest

# 7 NOV 24
def longestConsecutive_re(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    nums_set = set(nums)
    ans = 0
    for num in nums_set:
        if (num - 1) not in nums_set:
            cons = 1
            while num + 1 in nums_set:
                num += 1
                cons += 1
            ans = max(ans, cons)
    return ans
print(longestConsecutive_re(nums = [100,4,200,1,3,2]))