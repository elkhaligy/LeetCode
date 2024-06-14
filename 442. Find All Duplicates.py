# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        hash_table = {}
        for item in nums:
            if item not in hash_table:
                hash_table[item] = 1
            else:
                hash_table[item] += 1

        return [key for key, value in hash_table.items() if value == 2]


s = Solution()
print(s.findDuplicates([4,3,2,7,8,2,3,1]))