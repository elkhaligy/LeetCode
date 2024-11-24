def rotate(matrix: list[list[int]]) -> None:
    m, n = len(matrix), len(matrix[0])
    ans = [[0 for _ in range(m)] for _ in range(n)]
    print(ans)
    for i in range(m):
        for j in range(n):
            ans[i][j] = matrix[m - j - 1][i]

    matrix = ans
    pass


def rotate_inplace(matrix: list[list[int]]) -> None:
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
    print(matrix)
    # print(ans)
    # for i in range(m):
    #     for j in range(n):
    #         ans[i][j] = matrix[m - j - 1][i]

    # matrix = ans



def transpose_in_place(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):  # Only swap elements above the main diagonal
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

# Example
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose_in_place(matrix)
print(matrix)