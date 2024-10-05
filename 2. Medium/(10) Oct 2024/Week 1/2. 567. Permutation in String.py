def checkInclusion(s1: str, s2: str) -> bool:
    # Input: s1 = "ab", s2 = "eidbaooo"
    # If we sorted s1 = "ab", s2 = "eidbaooo"
    # then s1 must exist wihtin s2 sorted substring, otherwise it is false
    s1 = "".join(sorted(s1))

    for i in range(len(s2) - len(s1) + 1):
        if s1 == "".join(sorted(s2[i:i + len(s1)])):
            return True
    return False


print(checkInclusion(s1 = "ab", s2 = "eidboaoo"))
