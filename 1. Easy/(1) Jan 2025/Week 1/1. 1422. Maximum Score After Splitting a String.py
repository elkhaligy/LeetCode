def maxScoreBruteForce(s: str) -> int:
    ans = 0
    n = len(s)

    for i in range(n - 1):
        curr = 0
        for j in range(i + 1):
            if s[j] == "0":
                curr += 1
        
        for j in range(i + 1, n):
            if s[j] == "1":
                curr += 1
        
        ans = max(ans, curr)

    return ans

print(maxScoreBruteForce(s = "011101"))