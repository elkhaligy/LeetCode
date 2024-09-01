def construct2DArray(original: list[int], m: int, n: int) -> list[list[int]]:
    # Check if it is possible or not to create the matrix
    # Elements in the original list will not fit the matrix or will overflow the matrix
    if len(original) != m * n:
        return []
    
    matrix = [[0 for _ in range(n)] for _ in range(m)]

    cur_index = 0
    for i in range(m):
        for j in range(n):
            matrix[i][j] = original[cur_index]
            cur_index += 1
    
    return matrix


print(construct2DArray(original = [1,2,3,4], m = 2, n = 2))
