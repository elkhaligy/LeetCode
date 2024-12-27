def maxScoreSightseeingPair(values: list[int]) -> int:
    # Prepare values[i] + i
    firstTerm = [values[0]]
    for i in range(1, len(values)):
        newItem = values[i] + i
        if newItem > firstTerm[-1]:
            firstTerm.append(values[i] + i)
        else:
            firstTerm.append(firstTerm[-1])
    # Prepare values[j] - j
    secondTerm = []
    for i in range(len(values)):
        secondTerm.append(values[i] - i)

    ans = float('-inf')
    for i in range(1, len(values)):
        ans = max(ans, secondTerm[i] + firstTerm[i - 1])
    
    return ans

def maxScoreSightseeingPair_onePass(values: list[int]) -> int:
    n = len(values)
    firstTerm = [0] * n
    firstTerm[0] = values[0]
    ans = float('-inf')

    for i in range(1, n):
        currRightTerm = values[i] - i
        ans = max(ans, currRightTerm + firstTerm[i - 1])
        firstTerm[i] = max(firstTerm[i - 1], values[i] + i)
    
    return ans


def maxScoreSightseeingPair_onePass_withoutMax(values: list[int]) -> int:
    n = len(values)
    firstTerm = [0] * n
    firstTerm[0] = values[0]
    ans = 0

    for i in range(1, n):
        currRightTerm = values[i] - i
        if ans < currRightTerm + firstTerm[i - 1]:
            ans = currRightTerm + firstTerm[i - 1]
        if firstTerm[i - 1] > values[i] + i:
            firstTerm[i] = firstTerm[i - 1]
        else:
            firstTerm[i] = values[i] + i
    
    return ans

print(maxScoreSightseeingPair_onePass(values = [8,1,5,2,6]))