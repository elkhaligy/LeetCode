class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        max_or_value = 0
        for num in nums:
            max_or_value |= num
        
        return self.count_subsets(nums=nums, index=0, current_or=0, target=max_or_value)

    def count_subsets(self, nums: list[int], index: int, current_or: int, target: int) -> int:
        if index == len(nums):
            return 1 if current_or == target else 0

        no_pick = self.count_subsets(nums, index + 1, current_or, target)

        pick = self.count_subsets(nums, index + 1, current_or | nums[index], target)

        return no_pick + pick

sol_obj = Solution()
sol_obj.countMaxOrSubsets(nums = [3,1])