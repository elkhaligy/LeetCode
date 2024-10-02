class Solution:
    def shortestPalindrome(self, s: str) -> str:
        reversed_string = s[::-1]  

        for i in range(len(s)):
            if s[: len(s) - i] == reversed_string[i:]:
                return reversed_string[:i] + s
        return ""