class Solution:
    def minFlips(self, grid: list[list[int]]) -> int:
        # Check palindrom function
        def check_pal(arr: list[int]) -> int:
            left = 0
            right = len(arr) - 1
            flips = 0
            while left < right:
                if arr[left] != arr[right]:
                    flips += 1
                left += 1
                right -= 1
            return flips

        ans1 = 0
        for row in grid:
            ans1 += check_pal(row)
        
        transposed = [list(row) for row in zip(*grid)]
        ans2 = 0
        #print(transposed)
        for row in transposed:
            ans2 += check_pal(row)
        return min(ans1, ans2)
