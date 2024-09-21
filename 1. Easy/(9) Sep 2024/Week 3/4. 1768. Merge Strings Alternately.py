def mergeAlternately(word1: str, word2: str) -> str:
    answer = ""
    i = 0
    while i < len(word1) and i < len(word2):
        answer += word1[i]
        answer += word2[i]
        i += 1
    
    answer += word1[i:]
    answer += word2[i:]

    return answer

print(mergeAlternately(word1 = "ab", word2 = "pqrs"))