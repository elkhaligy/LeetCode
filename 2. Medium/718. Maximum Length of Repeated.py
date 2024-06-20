def findLength(nums1: list[int], nums2: list[int]) -> int:
    n, m = len(nums1), len(nums2)
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if nums1[i] == nums2[j]:
                if i > 0 and j > 0:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1
    
    max_so_far = 0
    for lst in dp:
        max_so_far = max(max_so_far, max(lst))
    
    return max_so_far


print(findLength(nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]))