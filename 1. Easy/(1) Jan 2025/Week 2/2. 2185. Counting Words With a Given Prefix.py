def prefixCount(words: list[str], pref: str) -> int:
    ans = 0
    for word in words:
        if word.find(pref) == 0:
            ans += 1
    return ans

print(prefixCount(words = ["pay","attention","practice","attend"], pref = "at"))
