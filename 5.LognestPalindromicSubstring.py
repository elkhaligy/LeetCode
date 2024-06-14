# https://leetcode.com/problems/longest-palindromic-substring/description/
# https://www.youtube.com/watch?v=uX0-xyPkR2w&list=PLFdAYMIVJQHO1paovM-tu2vtGzQU72z_U&index=3
# Brute force solution
class Solution(object):
    def palindrome(self, s):
        j = len(s) - 1
        i = 0
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Extract each substring
        # Test each substring for palindrom
        arrOfStrs = []
        for j in range(len(s)):
            for i in range(j, len(s)+1):
                sub = s[j:i]
                if self.palindrome(sub):
                    arrOfStrs.append(sub)
                    #print(sub)
        #print(max(arrOfStrs, key = len, default = ''))
        return max(arrOfStrs, key = len, default = '')


obj = Solution()
obj.longestPalindrome('cbbd')