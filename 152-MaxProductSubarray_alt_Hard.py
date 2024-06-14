# https://leetcode.com/problems/maximum-product-subarray/description/
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = max(nums)
        curMax = 1
        curMin = 1
        for n in nums:
            var = curMax * n
            curMax = max(n*curMax, n*curMin, n)
            curMin = min(var, n*curMin, n)
            ans = max(ans,curMax)
        return ans
    
obj = Solution()
print(obj.maxProduct([2,3,-2,4]))