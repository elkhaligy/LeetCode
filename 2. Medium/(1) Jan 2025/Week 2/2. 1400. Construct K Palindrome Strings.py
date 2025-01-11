from collections import Counter
def canConstruct(s: str, k: int) -> bool:
    # Total number of characters in s must be >= k
    n = len(s)
    if n < k:
        return False
    # If there's an odd frequency character then it must be 1 palindrom string
    # so if the this char count is > k then it is impossible for them to be k
    chrFreq = Counter(s)
    minPalin = 0
    for val in chrFreq.values():
        if val % 2 == 1:
            minPalin += 1
    if minPalin > k:
        return False
    return True


print(canConstruct(s = "annabelle", k = 2))
