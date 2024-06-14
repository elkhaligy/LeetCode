class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNeg = False
        if x < 0:
            x = x * -1
            isNeg = True
        tmp = x
        numLen = 0
        while tmp != 0:
            tmp //= 10
            numLen += 1
        print(numLen)
        res = 0
        i = 1
        while x != 0:
            rem = x%10
            x //= 10
            res += rem * (10 ** (numLen -i))
            i += 1
        
        if isNeg:
            res *= -1
        return res

obj = Solution()

obj.reverse(123)
            