class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        for c1 in t:
            s_index = 0
            t_index = 0
            total_len = 0
            while t_index < len(t) and s_index < len(s):
                if t[t_index] == s[s_index]:
                    t_index += 1
                    s_index += 1
                    total_len += 1
                else:
                    t_index += 1
            if total_len == len(s):
                return True
        return False