# https://leetcode.com/problems/maximum-product-subarray/description/
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        prod = 1
        ans = float('-inf')
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                prod *= nums[j]
                ans = max(ans,prod)
            prod = 1
        return ans
    
obj = Solution()
print(obj.maxProduct([2,3,-2,4]))