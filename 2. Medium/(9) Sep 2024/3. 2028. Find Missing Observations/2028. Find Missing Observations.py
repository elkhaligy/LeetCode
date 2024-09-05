def missingRolls(rolls: list[int], mean: int, n: int) -> list[int]:
    m = len(rolls)
    m_sum = sum(rolls)
    n_sum = mean * (n + m) - m_sum

    # Check if it is impossible to construct the rest of observations
    # If sum on n list is less than 6 * n, this is an impossible case as you won't be able to put observations larger than 6
    # If sum of n list is less than n, this is also an impossible case as you won't be able to put observations less than 1

    if 6 * n < n_sum or n_sum < n:
        return []

    # Now we operate on n_sum to extract the values
    quotient = n_sum // n
    remainder = n_sum % n
    # For example if n_sum is 12, then q is 6 and r is 0, we can then iterate over n and append q to our answer
    answer = []
    for _ in range(n):
        answer.append(quotient) # This can be written as answer = [quiotient] * n

    # Now lets handle the remainder
    for i in range(remainder):
        answer[i] += 1
    return answer


print(missingRolls(rolls = [1,5,6], mean = 3, n = 4))
