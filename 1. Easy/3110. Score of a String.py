def scoreOfString(s: str) -> int:
    n = len(s)
    next = 1
    ans = 0
    while next < n:
        ans += abs(ord(s[next - 1]) - ord(s[next]))
        next += 1
    return ans
    


print(scoreOfString("he"))