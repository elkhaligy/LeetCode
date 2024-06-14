# https://leetcode.com/problems/valid-parentheses/description/
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        data = {')' : '(', '}' : '{', ']' : '['}
        myStack = []
        for c in s:
            if c in data.values():
                myStack.append(c)
            elif c in data.keys():
                if myStack.pop() != data[c] or not myStack:
                    return False
            else:
                return False
        return len(myStack) == 0
    

obj = Solution()

print (obj.isValid("()"))