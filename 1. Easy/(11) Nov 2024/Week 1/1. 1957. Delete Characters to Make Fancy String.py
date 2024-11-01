def makeFancyString(s: str) -> str:
    ans = ""
    ans += s[0]
    couter = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            couter += 1
        else:
            couter = 0
        if couter < 3:
            couter += 1
            ans += s[i]

    return ans

print(makeFancyString(s = "aaabaaaa"))
