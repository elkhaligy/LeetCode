class Solution:
    def minLength(self, s: str) -> int:
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