def findRelativeRanks(score: list[int]) -> list[str]:
    sorted_scores = sorted(score, reverse=True)
    dct = {}
    for i in range(len(sorted_scores)):
        if i == 0:
            dct[sorted_scores[i]] = 'Gold Medal'
        elif i == 1:
            dct[sorted_scores[i]] = 'Silver Medal'
        elif i == 2:
            dct[sorted_scores[i]] = 'Bronze Medal'
        else:
            dct[sorted_scores[i]] = f"{i + 1}"
    

    ans = []
    for s in score:
        ans.append(dct[s])

    
    return ans

findRelativeRanks([10,3,8,9,4])