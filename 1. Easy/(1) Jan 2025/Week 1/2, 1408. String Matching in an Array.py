def stringMatching_BruteForce(words):
    n = len(words)
    answer = []

    for currWordInd in range(n):
        for otherWordInd in range(n):
            if currWordInd == otherWordInd:
                continue
            if words[currWordInd] in words[otherWordInd]:
                answer.append(words[currWordInd])
                break
    return answer

def stringMatching_Opt(words):
    pass

print(stringMatching_BruteForce(words = ["mass","as","hero","superhero"]))
