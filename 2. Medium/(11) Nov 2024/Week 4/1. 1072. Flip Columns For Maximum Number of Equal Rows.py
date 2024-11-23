from collections import defaultdict

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        count = defaultdict(int)

        for row in matrix:
            row_key = tuple(row)

            if row[0]:
                row_key = tuple([0 if n else 1 for n in row])

            count[row_key] += 1

        return max(count.values())
    
sol_obj = Solution()
sol_obj.maxEqualRowsAfterFlips(matrix = [[0,0,0],[0,0,1],[1,1,0]])