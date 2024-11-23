def rotateTheBox(box: list[list[str]]) -> list[list[str]]:
    rows = len(box)
    cols = len(box[0])
    rotatedBox = [[0 for _ in range(rows)] for _ in range(cols)]


    for i in range(rows):
        curr_row = box[i]
        for ptr1 in range(cols - 1, -1, -1):

            if curr_row[ptr1] == '.':
                for ptr2 in range(ptr1 - 1, -1, -1):
                    if curr_row[ptr2] == '.':
                        continue

                    if curr_row[ptr2] == '*':
                        break
                    
                    if curr_row[ptr2] == '#':
                        curr_row[ptr1], curr_row[ptr2] = curr_row[ptr2], curr_row[ptr1]
                        break



    new_rows = len(box[0])
    new_cols = len(box)

    for i in range(new_rows):
        for j in range(new_cols):
            rotatedBox[i][j] = box[rows - j - 1][i]
        # print(rotatedBox[i])

    return rotatedBox


rotateTheBox(box = [["#","#","*",".","*","."],
                    ["#","#","#","*",".","."],
                    ["#","#","#",".","#","."]])