def spiralMatrixIII_spagetti(rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
    # This solution works, but it is spagetti, because a lot of code is repeated, and a visited set is used to prevent duplicates elements, both of these areas can be improved
    number_of_elements = rows * cols
    ans = []
    start = [rStart, cStart]
    right_offset = 1
    bot_offset = 1
    left_offset = 2
    up_offset = 2
    visited = set()

    # Our loop stops when we finally have all of our elements
    while len(ans) != number_of_elements:

        # To the right
        for i in range(right_offset):
            if 0 <= start[0] < rows and 0 <= start[1] < cols and (start[0],start[1]) not in visited:
                ans.append([start[0], start[1]])
                visited.add((start[0], start[1]))
            start[1] += 1

        if 0 <= start[0] < rows and 0 <= start[1] < cols and (start[0],start[1]) not in visited:
            ans.append([start[0], start[1]])
            visited.add((start[0], start[1]))

        # To the bottom
        for i in range(bot_offset):
            if 0 <= start[0] < rows and 0 <= start[1] < cols and (start[0],start[1]) not in visited:
                ans.append([start[0], start[1]])
                visited.add((start[0], start[1]))
            start[0] += 1

        if 0 <= start[0] < rows and 0 <= start[1] < cols and (start[0],start[1]) not in visited:
            ans.append([start[0], start[1]])
            visited.add((start[0], start[1]))

        # To the left
        for i in range(left_offset):
            if 0 <= start[0] < rows and 0 <= start[1] < cols and (start[0],start[1]) not in visited:
                ans.append([start[0], start[1]])
                visited.add((start[0], start[1]))
            start[1] -= 1

        if 0 <= start[0] < rows and 0 <= start[1] < cols and (start[0],start[1]) not in visited:
            ans.append([start[0], start[1]])
            visited.add((start[0], start[1]))

        # To the up
        for i in range(up_offset):
            if 0 <= start[0] < rows and 0 <= start[1] < cols and (start[0],start[1]) not in visited:
                ans.append([start[0], start[1]])
                visited.add((start[0], start[1]))
            start[0] -= 1       

        if 0 <= start[0] < rows and 0 <= start[1] < cols and (start[0],start[1]) not in visited:
            ans.append([start[0], start[1]])
            visited.add((start[0], start[1]))

        right_offset += 2
        bot_offset += 2
        left_offset += 2
        up_offset += 2
    
    return ans

def spiralMatrixIII_cleaner(rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
    # This cleanedup solution doesn't need a visited set which speeds it up
    number_of_elements = rows * cols
    ans                = []
    cur_element        = [rStart, cStart]
    right_offset       = 1
    bot_offset         = 1
    left_offset        = 2
    up_offset          = 2
    check              = lambda a, b: 0 <= a < rows and 0 <= b < cols

    # Our loop stops when we finally have all of our elements
    while len(ans) != number_of_elements:
        # To the right
        for _ in range(right_offset):
            if check(cur_element[0], cur_element[1]):
                ans.append([cur_element[0], cur_element[1]])

            cur_element[1] += 1

        if check(cur_element[0], cur_element[1]):
            if cur_element[0] != ans[-1][0] and cur_element[1] != ans[-1][1]:
                ans.append([cur_element[0], cur_element[1]])

        # To the bottom
        for _ in range(bot_offset):
            if check(cur_element[0], cur_element[1]):
                ans.append([cur_element[0], cur_element[1]])

            cur_element[0] += 1

        if check(cur_element[0], cur_element[1]):
            if cur_element[0] != ans[-1][0] and cur_element[1] != ans[-1][1]:
                ans.append([cur_element[0], cur_element[1]])

        # To the left
        for _ in range(left_offset):
            if check(cur_element[0], cur_element[1]):
                ans.append([cur_element[0], cur_element[1]])

            cur_element[1] -= 1

        if check(cur_element[0], cur_element[1]):
            if cur_element[0] != ans[-1][0] and cur_element[1] != ans[-1][1]:
                ans.append([cur_element[0], cur_element[1]])

        # To the up
        for _ in range(up_offset):
            if check(cur_element[0], cur_element[1]):
                ans.append([cur_element[0], cur_element[1]])

            cur_element[0] -= 1

        if check(cur_element[0], cur_element[1]):
            if cur_element[0] != ans[-1][0] and cur_element[1] != ans[-1][1]:
                ans.append([cur_element[0], cur_element[1]])

        right_offset += 2
        bot_offset   += 2
        left_offset  += 2
        up_offset    += 2

    
    return ans


print(spiralMatrixIII_cleaner(rows = 5, cols = 6, rStart = 1, cStart = 4))