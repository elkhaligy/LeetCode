def vowelStrings(words: list[str], queries: list[list[int]]) -> list[int]:
    queriesLen = len(queries)
    wordsLen = len(words)
    ans = [0] * queriesLen
    prefix = [0] * wordsLen # Each index in the prefix array tells how many valid strings are there from the start of the list till that index inclusive
    vowels = {"a", "e", "i", "o", "u"}

    # Construct prefix vowels
    currSum = 0
    for i in range(wordsLen):
        firstLetter = words[i][0]
        lastLetter = words[i][-1]
        if firstLetter in vowels and lastLetter in vowels:
            currSum += 1
        prefix[i] = currSum
    #print(prefix)

    for i in range(queriesLen):
        currQuery = queries[i]
        if currQuery[0] == 0:
            ans[i] = prefix[currQuery[1]]
        else:
            ans[i] = prefix[currQuery[1]] - prefix[currQuery[0] - 1]

    return ans

print(vowelStrings(words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]))