# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        ans = []
        for item in nums:
            if nums[abs(item) - 1] < 0:
                ans.append(abs(item))
            else:
                nums[abs(item) - 1] *= -1
        
        return ans


s = Solution()
print(s.findDuplicates([4,3,2,7,8,2,3,1]))