# https://leetcode.com/problems/maximum-product-subarray/description/

# https://www.youtube.com/watch?v=Y6B-7ZctiW8
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftProd = 1
        rightProd = 1
        ans = nums[0]

        for i in range(len(nums)):
            if leftProd == 0:
                leftProd = 1
            if rightProd == 0:
                rightProd = 1
            leftProd *= nums[i]
            rightProd *= nums[len(nums)-1-i]
            ans = max(ans,leftProd,rightProd)
        return ans
    
obj = Solution()
print(obj.maxProduct([2,3,-2,4]))