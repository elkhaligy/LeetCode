# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashTable = {}
        for i in range(len(numbers)):
        # target = number1 + number2, number2 = target - number1
            if numbers[i] in hashTable:
                return [hashTable[numbers[i]]+1,i+1]
            hashTable[target-numbers[i]] = i
    
obj = Solution()
print(obj.twoSum([2,7,11,15],9))
