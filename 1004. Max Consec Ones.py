class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l = r = 0

        num_zeros = 0
        max_so_far = 0
        while r < len(nums):
            if num_zeros > k:
                while(num_zeros > k):
                    if nums[l] == 1:
                        l += 1
                    elif nums[l] == 0:
                        l += 1
                        num_zeros -= 1  
            if nums[r] == 0:
                num_zeros += 1
            if num_zeros == k:
                max_so_far = max(max_so_far, r - l + 1)


            r += 1

        print(max_so_far)


sol_obj = Solution()
sol_obj.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3)