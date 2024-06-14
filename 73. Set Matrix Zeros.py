def setZeroes(matrix: list[list[int]]) -> None:
    m = len(matrix)
    n = len(matrix[0])
    zeros_loc = []
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zeros_loc.append((i, j))
    print(zeros_loc)
    for zero_tup in zeros_loc:
        # zero the row
        for i in range(n):
            matrix[zero_tup[0]][i] = 0
        # zero the col
        for i in range(m):
            matrix[i][zero_tup[1]] = 0


matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setZeroes(matrix)
print(matrix)