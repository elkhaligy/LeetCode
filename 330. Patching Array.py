from collections import Counter, defaultdict

def minPatches(nums: list[int], n: int) -> int:
    missing_sum = 1
    ans = 0
    i = 0
    
    while missing_sum <= n:
        if i < len(nums) and nums[i] <= missing_sum:
            missing_sum += nums[i]
            i += 1
        else:
            missing_sum *= 2
            ans += 1
        
    return ans
print(minPatches(nums = [1, 5, 10], n = 20))