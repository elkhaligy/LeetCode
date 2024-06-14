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
        # odd length

        left = 0
        right = len(s) - 1
        for i in range(len(s)):
            left = i
            right = i
            while left != -1 and right < len(s):
                sub = s[left:right+1]
                print(sub)
                if self.palindrome(sub):
                    arrOfStrs.append(sub)
                left -= 1
                right += 1

       # even length
        left = 0
        right = len(s) - 1
        for i in range(len(s)):
            left = i
            right = i
            while left != -1 and right < len(s):
                sub = s[left:right+2]
                print(sub)
                if self.palindrome(sub):
                    arrOfStrs.append(sub)
                left -= 1
                right += 1
        return max(arrOfStrs, key = len, default = '')

obj = Solution()
obj.longestPalindrome('abba')