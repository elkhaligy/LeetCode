class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_now = 0
        a = k
        max_list = []
        for r in range(len(s)):
            if s[l] == s[r]:
                max_now += 1
            else:
                if a != 0:
                    max_now += 1
                    a -= 1
                else:
                    max_list.append(max_now)
                    max_now = 1
                    l = r

        max_now = 0
        s = s[::-1]
        l = 0
        a = k
        for r in range(len(s)):
            if s[l] == s[r]:
                max_now += 1
            else:
                if a != 0:
                    max_now += 1
                    a -= 1
                else:
                    max_list.append(max_now)
                    max_now = 1
                    l = r
        print(max_list)
        max_list.append(max_now)
        print(max(max_list))

sol_obj = Solution()
sol_obj.characterReplacement("ABBB", 2)
