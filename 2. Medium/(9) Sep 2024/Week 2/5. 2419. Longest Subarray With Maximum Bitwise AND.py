class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        max_num = max(nums)
        cur_longest = 0
        answer = 0
        for num in nums:
            if num == max_num:
                cur_longest += 1
            else:
                cur_longest = 0
            answer = max(answer, cur_longest)
        return answer