def restoreMatrix(rowSum, colSum):
    row_len, col_len = len(rowSum), len(colSum)

    curr_row_sum = [0] * row_len
    curr_col_sum = [0] * col_len

    orig_matrix = [[0] * col_len for _ in range(row_len)]

    for i in range(row_len):
        for j in range(col_len):
            orig_matrix[i][j] = min(rowSum[i] - curr_row_sum[i], colSum[j] - curr_col_sum[j])

            curr_row_sum[i] += orig_matrix[i][j]
            curr_col_sum[j] += orig_matrix[i][j]

    return orig_matrix