def championFinder(n: int, edgeList: list[list[int]]) -> int:
    inDegree = [0] * n

    for edge in edgeList:
        inDegree[edge[1]] += 1
    
    currentZeroIndex = -1
    for index, degree in enumerate(inDegree):
        if degree == 0:
            if currentZeroIndex != -1:
                return -1
            currentZeroIndex = index
    
    return currentZeroIndex

def championFinder_Sol2(n: int, edgeList: list[list[int]]) -> int:
    pointedAt = [0] * n

    for edge in edgeList:
        pointedAt[edge[1]] = 1
    
    currentZeroIndex = -1
    for index, pointed in enumerate(pointedAt):
        if pointed == 0:
            if currentZeroIndex != -1:
                return -1
            currentZeroIndex = index
    
    return currentZeroIndex
print(championFinder(n = 3, edgeList = [[0,1],[1,2]]))
