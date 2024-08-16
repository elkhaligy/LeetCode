class Solution:
    def maxDistance_bruteforce(self, arrays: list[list[int]]) -> int:
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_dist = 0

        for i in range(1, len(arrays)):
            curr_min = arrays[i][0]
            curr_max = arrays[i][-1]

            max_dist = max(max_dist, max(abs(curr_max - min_val), abs(max_val - curr_min)))

            min_val = min(min_val, curr_min)
            max_val = max(max_val, curr_max)

        return max_dist
        
obj = Solution()
print(obj.maxDistance_bruteforce([[-1,1],[-3,1,4],[-2,-1,0,2]]))