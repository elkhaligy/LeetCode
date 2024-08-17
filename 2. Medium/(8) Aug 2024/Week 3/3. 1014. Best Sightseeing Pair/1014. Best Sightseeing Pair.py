def maxScoreSightseeingPair_bruteforce(values: list[int]) -> int:
    # O(n2) solution
    n = len(values)
    score = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            score = max(score, values[i] + values[j] + i - j)
    
    return score

def maxScoreSightseeingPair_dp_3pass(values: list[int]) -> int:
    n = len(values)

    first_term_list = [values[0]]
    for i in range(1, n):
        first_term_list.append(max(first_term_list[-1], values[i] + i))
    
    second_term_list = [0]
    for i in range(1, n):
        second_term_list.append(values[i] - i)
    #print(first_term_list, second_term_list)

    score = 0
    for i in range(1, n):
        score = max(score, second_term_list[i] + first_term_list[i - 1])
    
    return score


def maxScoreSightseeingPair_dp_1pass(values: list[int]) -> int:
    n = len(values)
    max_first_term = values[0]
    score = 0

    for i in range(1, n):
        score = max(score, values[i] - i + max_first_term)
        max_first_term = max(max_first_term, values[i] + i)
        

    return score
print(maxScoreSightseeingPair_dp_1pass(values = [8,1,5,2,6]))