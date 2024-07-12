def characterReplacement_fail(s: str, k: int) -> int:
    l = 0
    max_now = 0
    a = k
    max_list = []
    for r in range(len(s)):
        if s[l] == s[r]:
            max_now += 1
        else:
            if a != 0:
                max_now += 1
                a -= 1
            else:
                max_list.append(max_now)
                max_now = 1
                l = r

    max_now = 0
    s = s[::-1]
    l = 0
    a = k
    for r in range(len(s)):
        if s[l] == s[r]:
            max_now += 1
        else:
            if a != 0:
                max_now += 1
                a -= 1
            else:
                max_list.append(max_now)
                max_now = 1
                l = r
    print(max_list)
    max_list.append(max_now)
    print(max(max_list))

import collections
def characterReplacement_sliding_window(s: str, k: int) -> int:
    frequency_dct = collections.defaultdict(int)

    left, right = 0, 0
    longest = 0
    while right < len(s):
        frequency_dct[s[right]] += 1

        while (right - left + 1) - max(frequency_dct.values()) > k:
            frequency_dct[s[left]] -= 1
            left += 1
            
        longest = max(longest, right - left + 1)
        right += 1
    
    return longest

print(characterReplacement_sliding_window(s = "AABABBA", k = 1))