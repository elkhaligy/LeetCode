from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mg_counter = Counter(magazine)

        for c in ransomNote:
            if c in mg_counter and mg_counter[c] > 0:
                mg_counter[c] -= 1
            else:
                return False

        return True