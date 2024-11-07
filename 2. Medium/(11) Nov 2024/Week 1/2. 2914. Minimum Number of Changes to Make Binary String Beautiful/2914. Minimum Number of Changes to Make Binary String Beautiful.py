def minChanges(s: str) -> int:
    ans = 0
    for i in range(0, len(s) - 1, 2):
        if s[i] != s[i + 1]:
            ans += 1

    return ans

print(minChanges(s = "1001"))
