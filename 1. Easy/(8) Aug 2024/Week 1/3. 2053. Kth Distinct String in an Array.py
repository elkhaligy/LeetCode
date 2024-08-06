from collections import Counter
class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        freq = Counter(arr)

        for c in arr:
            if freq[c] == 1:
                k -= 1
            if k <= 0:
                return c
                
        return ""