def longestCommonSubsequence(text1: str, text2: str) -> int:

    def find_longest(text1, text2):
        longest = 0
        cur = 0
        cnt = 0
        start_1 = 0
        start_2 = 0
        while cnt < len(text2):
        
            for i in range(start_2, len(text2)):
                for j in range(start_1, len(text1)):
                    if text2[i] == text1[j]:
                        cur += 1
                        start_1 = j + 1
                        break
            
            longest = max(longest, cur)
            cur = 0
            start_2 += 1
            start_1 = 0
            cnt += 1
        return longest

    longest1 = find_longest(text1, text2)
    longest2 = find_longest(text2, text1)
    
    return max(longest1, longest2)



print(longestCommonSubsequence(text1 = "ylqpejqbalahwr", text2 = "yrkzavgdmdgtqpg" ))