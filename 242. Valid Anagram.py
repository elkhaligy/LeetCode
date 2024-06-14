from collections import Counter
def isAnagram_oNlogN(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

def isAnagram_oN(s: str, t: str) -> bool:
    occu_dict1 = Counter(s)
    occu_dict2 = Counter(t)
    return occu_dict1 == occu_dict2



print(isAnagram_oN( s = "rat", t = "tar"))