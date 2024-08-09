def numMagicSquaresInside(grid: list[list[int]]) -> int:
    num_rows = len(grid)
    num_cols = len(grid[0])
    ans      = 0
    if num_rows < 3 or num_cols < 3: 
        return 0
    
    rows = []
    cols = []
    flag = False

    for k in range(num_rows - 3 + 1): # Row control
        for f in range(num_cols - 3 + 1): # Column control

            # Populate rows from the inner 3x3 matrices
            rows = []
            for i in range(k, 3 + k):
                cur_row = []
                for j in range(f, 3 + f):
                    # Check the 1 to 9 inclusive condition
                    if grid[i][j] > 9 or grid[i][j] == 0:
                        flag = True
                    cur_row.append(grid[i][j])
                rows.append(cur_row)
            cols = [list(a) for a in zip(*rows)]
            #print(rows)

            # Check distinct elements condition
            for i in range(3):
                if len(rows[i]) != len(set(rows[i])):
                    flag = True
                    break


            if not flag: # Flag become true if any number is 0 or above 9, and if two numbers are the same
                # Obtain the sums from columns and rows
                sums = []
                for l in range(3):
                    sums.append(sum(rows[l]))
                    sums.append(sum(cols[l]))
                sums.append(rows[0][0] + rows[1][1] + rows[2][2])
                #print(sums)

                # If all the values are equal in the sums list then it is a magic square
                if all(x == sums[0] for x in sums):
                    ans += 1

            # Resetting the condition flag
            flag = False

    return ans

print(numMagicSquaresInside([[3,10,2,3,4],
                             [4,5 ,6,8,1],
                             [8,8 ,1,6,8],
                             [1,3 ,5,7,1],
                             [9,4 ,9,2,9]]))
