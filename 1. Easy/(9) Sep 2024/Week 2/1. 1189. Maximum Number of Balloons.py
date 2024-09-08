class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_freq = {} # a map that contains char : it's frequency
        for c in text:
            if c not in char_freq:
                char_freq[c] = 1
            else:
                char_freq[c] += 1
        
        word = "balloon"
        answer = 0

        while True:
            for c in word:
                if c in char_freq and char_freq[c] > 0:
                    char_freq[c] -= 1
                else:
                    return answer
            answer += 1