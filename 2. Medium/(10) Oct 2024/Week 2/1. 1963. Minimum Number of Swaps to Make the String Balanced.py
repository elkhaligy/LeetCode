class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        answer = 0
        for ch in s:
            # If openning append
            if ch == "[":
                stack.append(ch)
            # If not oppening pop, but if the stack is empty then unbalanced parenthesis found
            else:
                if stack:
                    stack.pop()
                else:
                    answer += 1
        return (answer + 1) // 2