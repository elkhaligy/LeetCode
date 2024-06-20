
def checkPalindrome(s):
    if len(s) == 1:
        return True
    if len(s) % 2 == 0:
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return False
    else:
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return False
    return True
def longestPalindrome_brute_force(s: str) -> str:
    dct = {}
    for i in range(len(s)):
        for j in range(i, len(s)):
            if checkPalindrome(s[i:j + 1]):
                dct[s[i:j + 1]] = len(s[i:j + 1])
    
    print(dct)

def longestPalindrome(s: str) -> str:
    ans = {}
    if len(s) <= 1:
        return s
    # odd length palindroms
    for i in range(len(s)):
        ans[s[i]] = len(s[i])
        l = i - 1
        r = i + 1
        while l > -1 and r < len(s):
            if s[l] == s[r]:
                ans[s[l:r+1]] = len(s[l:r+1])
                l -= 1
                r += 1
            else:
                break
    # even length palindroms
    for i in range(len(s)):
        ans[s[i]] = len(s[i])
        l = i - 1
        r = i
        while l > -1 and r < len(s):
            if s[l] == s[r]:
                ans[s[l:r+1]] = len(s[l:r+1])
                l -= 1
                r += 1
            else:
                break
   # print(ans)
    return max(ans,key=ans.get)

print(longestPalindrome('aba'))