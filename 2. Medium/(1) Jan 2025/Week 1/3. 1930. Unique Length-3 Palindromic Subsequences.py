def countPalindromicSubsequence(s: str) -> int:
    # We can use a prefix algorithm
    # at each character we need to find the same character to the right of this character
    # while we'r finding this character we need to count the number of characters in between them

    # for example s = "aabca"
    # for the first character, it is a, get the occurence of the 'a' but from the right
    # now count the unique characters in between them, it gives 3

    # abc
    answer = 0
    sSet = set(s)
    for char in sSet:
        leftIndex = s.index(char)
        rightIndex = s.rindex(char)
        betweenSet = set(s[leftIndex + 1:rightIndex])
        #print(f"between set now = {betweenSet}")
        answer += len(betweenSet)

    return answer

print(countPalindromicSubsequence(s = "aabca"))