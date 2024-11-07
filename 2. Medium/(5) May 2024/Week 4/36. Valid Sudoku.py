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

# 7 Nov 24
def isValidSudoku_opt(board: list[list[str]]) -> bool:
    # Check row duplicates
    for i in range(9):
        s = set()
        for j in range(9):
            item = board[i][j]
            if item in s:
                return False
            elif item != '.':
                s.add(item)

    # Check col duplicates
    for i in range(9):
        s = set()
        for j in range(9):
            item = board[j][i]
            if item in s:
                return False
            elif item != '.':
                s.add(item)
    
    # Check repetitive 3x3 numbers
    starts = [(0, 0), (0, 3), (0, 6),
              (3, 0), (3, 3), (3, 6),
              (6, 0), (6, 3), (6, 6)]
    for i, j in starts:
        s = set()
        for row in range(i, i + 3):
            for col in range(j, j + 3):
                item = board[row][col]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)
    return True

print(isValidSudoku_opt(board = 
[[".","4",".",".",".",".",".",".","."],
 [".",".","4",".",".",".",".",".","."],
 [".",".",".","1",".",".","7",".","."],
 [".",".",".",".",".",".",".",".","."],
 [".",".",".","3",".",".",".","6","."],
 [".",".",".",".",".","6",".","9","."],
 [".",".",".",".","1",".",".",".","."],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","8",".",".",".",".","."]]))