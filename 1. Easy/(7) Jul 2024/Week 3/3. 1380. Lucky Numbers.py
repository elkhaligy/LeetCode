def luckyNumbers_bruteforce(matrix: list[list[int]]) -> list[int]:
        n, m = len(matrix), len(matrix[0])
        # [3   , 7,    8]
        # [9   , 11,  13]
        # [15  , 16,  17]

        row_min = [] # size of n, [3, 9, 15]
        for i in range(n):
            cur_min = float('inf')
            for j in range(m):
                cur_min = min(cur_min, matrix[i][j])
            row_min.append(cur_min)

        col_max = [] # size of m, [15, 16, 17]
        for i in range(m):
            cur_max = float('-inf')
            for j in range(n):
                cur_max = max(cur_max, matrix[j][i])
            col_max.append(cur_max)

        answer = [] 
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == row_min[i] and matrix[i][j] == col_max[j]:
                    answer.append(matrix[i][j])

        return answer

