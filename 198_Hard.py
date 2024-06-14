# https://leetcode.com/problems/house-robber/
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p1=0
        p2=0
        ans=0
        for i in range(len(nums)):
            ans = max(nums[i]+p1,p2)
            p1=p2
            p2=ans
        return ans

obj = Solution()
print(obj.rob([2,7,9,3,1]))