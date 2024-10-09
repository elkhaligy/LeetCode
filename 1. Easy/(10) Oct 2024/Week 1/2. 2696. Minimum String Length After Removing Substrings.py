class Solution:
    def minLength_n2(self, s: str) -> int:
        while True:
            if "AB" in s:
                new_str = s.replace("AB", "")
                s = new_str
            elif "CD" in s:
                new_str = s.replace("CD", "")
                s = new_str
            else:
                break
        return len(s)
    
    def minLength_n(self, s: str) -> int:
        # We can optimize the solution using a stack
        stack = []

        for ch in s:
            if not stack:
                stack.append(ch)
                continue
            if stack[-1] == "A" and ch == "B":
                stack.pop()
            elif stack[-1] == "C" and ch == "D": 
                stack.pop()
            else:
                stack.append(ch)

        return len(stack)