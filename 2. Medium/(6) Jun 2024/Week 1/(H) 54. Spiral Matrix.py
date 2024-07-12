# This problem is great on making logic out of multiple indices together
# I looked at the solution and now I fully understand it, the way I visualized it
# is with the highlighter more that the indices themselves, so the highlighter wins
def spiralOrder(matrix: list[list[int]]) -> list[int]: 
    rows, cols = len(matrix), len(matrix[0])

    top, bottom, left, right = 0, rows - 1, 0, cols - 1
    result = []

    while len(result) < rows * cols:

        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    return result
    
print(spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))


