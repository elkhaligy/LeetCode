def maxMatrixSum(matrix: list[list[int]]) -> int:
    totalSum = totalNegatives = 0
    minSoFar = float('inf')
    n = len(matrix)

    for row in range(n):
        for col in range(n):
            if matrix[row][col] < 0:
                totalNegatives += 1
            minSoFar = min(minSoFar, abs(matrix[row][col]))
            totalSum += abs(matrix[row][col])
    if totalNegatives % 2 != 0:
        totalSum -= 2 * minSoFar
    
    return totalSum

print(maxMatrixSum(matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]))
