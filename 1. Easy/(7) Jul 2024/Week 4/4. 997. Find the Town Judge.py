def findJudge(n: int, trust: list[list[int]]) -> int:
    # Directional graph
    number_trusting = [0] * (n + 1) # number of people trusting in a node
    for edge in trust:
        number_trusting[edge[1]] += 1

    trusting = set() # people that are trusting other people
    for node in trust:
        trusting.add(node[0])

    for i in range(1, n + 1):
        if i not in trusting and number_trusting[i] == n - 1:
            return i
    return -1