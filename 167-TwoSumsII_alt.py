# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        rP = len(numbers) - 1
        lP = 0
        while lP != rP:
            if numbers[rP] + numbers[lP] > target:
                rP-=1
            elif numbers[rP] + numbers[lP] != target:
                lP+=1
            else:
                return [lP+1,rP+1]
            
    
obj = Solution()
print(obj.twoSum([2,7,11,15],9))
