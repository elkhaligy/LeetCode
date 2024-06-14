# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution(object):
    def strStr(self, haystack: str, needle: str):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

obj = Solution()
print (obj.strStr("leetcode", "leeto"))
        