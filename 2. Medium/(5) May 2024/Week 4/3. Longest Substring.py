class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        ans = 0
        while r < len(s):
            if s[r] == s[l]:
                l += 1
                r += 1
            else:
                r += 1
            if len(set(s[l:r + 1])) == len(s[l : r+1]):
                ans = max(ans, len(s[l : r+1]))
            else:
                l += 1

    def lengthOfLongestSubstring_Sol2(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        occu = set()
        l = 0
        r = 1
        ans = 0
        occu.add(s[l])
        while r < len(s):
            while s[r] in occu:
                occu.remove(s[l])
                l += 1
            occu.add(s[r])
            r += 1
            #print(len(occu))
            ans = max(ans, len(occu))
           
        return ans


sol_obj = Solution()

print(sol_obj.lengthOfLongestSubstring_Sol2("qrsvbspk"))