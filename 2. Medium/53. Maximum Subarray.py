# https://leetcode.com/problems/maximum-subarray/
def maxSubArray_bruteforce(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    sum = 0
    ans = float('-inf')
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            sum += nums[j]
            ans = max(ans,sum)
        sum = 0
    return ans

def maxSubArray_greedy(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    sum = 0
    ans = float('-inf')
    
    for i in range(len(nums)):
        sum+=nums[i]
        ans = max(ans,sum)
        if sum<0:
            sum = 0     
    return ans

print(maxSubArray_greedy([-2,1,-3,4,-1,2,1,-5,4]))