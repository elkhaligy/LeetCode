# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        max_sf = 0
        # for r in range(len(height)):
        #     if l != r:
        #         max_sf = max( min(height[r], height[l]) * ((r - l)), max_sf)
        #     if height[r] > height[l]:
        #         l = r

        while r > l:
            max_sf = max( min(height[r], height[l]) * ((r - l)), max_sf)

            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        
        
        print(max_sf)



sol_obj = Solution()

sol_obj.maxArea([1,2,4,3])