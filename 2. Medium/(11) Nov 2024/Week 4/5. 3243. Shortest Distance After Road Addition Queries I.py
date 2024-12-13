def shortestDistance(n: int, queries: list[list[int]]):
    edgeList = []
    # if n = 5
    # 0, 1, 2, 3, 4, 5
    # [[1], [2], [3], [4], [5]]
    for i in range(n):
        edgeList.append([i + 1])


    print(edgeList)


print(shortestDistance(n = 3, queries = [[0,1],[1,2]]))