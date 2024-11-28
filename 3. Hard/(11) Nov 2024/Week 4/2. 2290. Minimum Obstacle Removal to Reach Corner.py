import heapq
def minimumObstacles(grid: list[list[int]]) -> int:
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def isValidCell(cell: tuple):
        return 0 <= cell[0] < len(grid) and 0 <= cell[1] < len(grid[0])

    m, n = len(grid), len(grid[0])

    obstaclesCount = [[float("inf") for _ in range(n)] for _ in range(m)]
    obstaclesCount[0][0] = grid[0][0]

    priorityQueue = [(obstaclesCount[0][0], 0, 0)]

    while priorityQueue:
        obstacleValue, row, col = heapq.heappop(priorityQueue)

        if row == m - 1 and col == n - 1:
            return obstacleValue
        
        for x, y in directions:
            newRow = row + x
            newCol = col + y

            if isValidCell((newRow, newCol)):
                newObstacleValue = obstacleValue + grid[newRow, newCol]

                if newObstacleValue < obstaclesCount[newRow][newCol]:
                    obstaclesCount[newRow][newCol] = newObstacleValue
                    heapq.heappush(priorityQueue ,(newObstacleValue, newRow, newCol))
    return obstaclesCount[m - 1][n - 1]


print(minimumObstacles(grid = [[0,1,1],[1,1,0],[1,1,0]]))
