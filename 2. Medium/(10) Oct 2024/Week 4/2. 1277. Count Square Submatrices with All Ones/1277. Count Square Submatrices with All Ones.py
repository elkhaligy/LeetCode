def countSquares_bottomUpDP(matrix: list[list[int]]) -> int:
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    answer = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            answer += dp[i][j]

    return answer


print(countSquares_bottomUpDP(matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]))
