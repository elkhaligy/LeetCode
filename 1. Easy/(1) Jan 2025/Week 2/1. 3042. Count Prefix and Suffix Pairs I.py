def countPrefixSuffixPairs_Bruteforce(words: list[str]) -> int:
    n = len(words) # Number of words, min = 1, max = 50
    if n == 1:
        return 0
    def isPrefixAndSuffix(str1, str2) -> bool:
        if str2.find(str1) == 0 and str2.rfind(str1) == len(str2) - len(str1):
            return True
        return False

    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            ans += 1 if isPrefixAndSuffix(words[i], words[j]) else 0
        
    return ans

print(countPrefixSuffixPairs_Bruteforce(words = ["a","aba","ababa","aa"]))