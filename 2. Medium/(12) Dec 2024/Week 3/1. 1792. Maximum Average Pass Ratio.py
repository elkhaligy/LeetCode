import heapq

def maxAverageRatio(classes: list[list[int]], extraStudents: int) -> float:
    maxHeap = []

    def getAverageIncrement(passStudents: int, totalStudents: int) -> int:
        currAvg = passStudents / totalStudents
        newAvg = (passStudents + 1) / (totalStudents + 1)
        return newAvg - currAvg
    
    for index, currClass in enumerate(classes):
        passStudents = currClass[0]
        totalStudents = currClass[1]
        currAvgIncrement = getAverageIncrement(passStudents, totalStudents)
        heapq.heappush(maxHeap, (-currAvgIncrement, index))
    
    # print(maxHeap)

    while extraStudents != 0:
        _, index = heapq.heappop(maxHeap)
        classes[index][0] += 1
        classes[index][1] += 1
        currAvgIncrement = getAverageIncrement(classes[index][0], classes[index][1])
        heapq.heappush(maxHeap, (-currAvgIncrement, index))
        extraStudents -= 1
    
    finalAvg = sum((currClass[0] / currClass[1]) for currClass in classes) / len(classes)

    return finalAvg

print(maxAverageRatio(classes = [[1,2],[3,5],[2,2]], extraStudents = 2))
