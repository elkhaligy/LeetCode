class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        lst = [0] * (n + 1)
        lst[1] = 1
        lst[2] = 2

        for i in range(3, n + 1):
            lst[i] = lst[i - 1] + lst[i -2]
        
        return lst[-1]


s = Solution()
s.climbStairs(4)
            