class Solution:
    # This is a brute force solution
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        # Prefix sum array
        prefix_list = [0]
        for num in nums:
            prefix_list.append(num + prefix_list[-1])
        
        # Extract all sums from the prefix sum array
        sums = []
        n = len(prefix_list)
        for i in range(n - 1):
            for j in range(i + 1, n):
                sums.append(prefix_list[j] - prefix_list[i])
        
        sums.sort()
        ans = 0
        for i in range(left - 1, right):
            ans += sums[i]
        #print(prefix_list, sums)
        return ans % (1000000000 + 7)