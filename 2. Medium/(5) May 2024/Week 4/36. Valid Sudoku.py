from collections import Counter
from collections import defaultdict
def get_occu_3x3(board, row, col) -> dict:
    occu_dict = defaultdict(int)
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            if board[i][j].isnumeric():
                occu_dict[board[i][j]] += 1
    
    return occu_dict

def isValidSudoku(board: list[list[str]]) -> bool:
    for row in board:
        row_occu_dict = Counter(row)
        for key, value in row_occu_dict.items():
            if key.isnumeric() and value > 1:
                return False
            
    transposed_board = list(zip(*board))
    for col in transposed_board:
        col_occu_dict = Counter(col)
        for key, value in col_occu_dict.items():
            if key.isnumeric() and value > 1:
                return False
    # rows
    # 0 to 2
    # 3 to 5
    # 6 to 8

    # cols
    # same
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            occu_dict = get_occu_3x3(board, i, j)
            for key, value in occu_dict.items():
                if key.isnumeric() and value > 1:
                    return False
    return True

print(isValidSudoku(board = 
[[".","4",".",".",".",".",".",".","."],
 [".",".","4",".",".",".",".",".","."],
 [".",".",".","1",".",".","7",".","."],
 [".",".",".",".",".",".",".",".","."],
 [".",".",".","3",".",".",".","6","."],
 [".",".",".",".",".","6",".","9","."],
 [".",".",".",".","1",".",".",".","."],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","8",".",".",".",".","."]]))