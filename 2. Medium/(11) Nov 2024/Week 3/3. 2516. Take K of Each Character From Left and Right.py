from collections import Counter

# Good problem with a unique idea, in sliding window problems, we always looked inside the window, but in this one we looked outside the window too
def takeKchars(s: str, k: int):
    windowFreq = {"a" : 0, "b" : 0, "c" : 0}
    left = right = windowSize = 0
    
    # Handle impossible case
    freqCounter = Counter(s)
    if len(freqCounter.keys()) != 3:
        return -1
    for value in freqCounter.values():
        if value < k:
            return -1
    
    # The idea here is to keep track of the character outside the window!!!
    while right < len(s):
        windowFreq[s[right]] += 1

        while left <= right and (freqCounter['a'] - windowFreq['a'] < k or freqCounter['b'] - windowFreq['b'] < k or freqCounter['c'] - windowFreq['c'] < k):
            windowFreq[s[left]] -= 1
            left += 1

        windowSize = max(windowSize, right - left + 1)
        right += 1
        
    return len(s) - windowSize
print(takeKchars(s = "aabaaaacaabc", k = 2))